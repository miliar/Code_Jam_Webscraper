#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cond2(int X, int minCR, int maxCR){
    if(X < 2*minCR){
        return false;
    }
    int remX = X - minCR;
    for(int jut=1; jut <= remX/2; jut++){
        bool flag = true;
        for(int fr=0; fr <= maxCR-(remX+1); fr++){
            int num_squares = (fr+jut)*minCR - jut;
            if(num_squares % X == 0)
                flag = false;
        }
        if(flag == true)
            return true;
    }
    return false;
}

void solve(int case_num){
    int X, R, C;
    cin >> X >> R >> C;
    string winner;
    int minCR = min(C,R);
    int maxCR = max(C,R);
    bool cond1 = minCR >= 3 && (X >= 7);
    bool cond3 = ((C*R)%X) != 0;
    bool cond4 = X > maxCR;
    bool cond5 = ((X+1)/2) > minCR;

    if(cond1 || cond2(X, minCR, maxCR) || cond3 || cond4 || cond5){
        winner = "RICHARD";
    }
    else{
        winner = "GABRIEL";
    }
    printf("Case #%d: %s\n", case_num, winner.c_str());

}

int main(){
    int num_cases;
    cin >> num_cases;
    for(int ii=1; ii <= num_cases; ++ii)
        solve(ii);
}

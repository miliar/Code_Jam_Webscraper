#include <set>
#include <fstream>
//#include <iostream>
using namespace std;

ifstream cin("A-small-attempt0.in");
ofstream cout("A.txt");

void read(int& r, int A[][4]){
    cin >> r;
    r--;
    for(int i = 0; i < 4; i++){
        for(int j = 0; j < 4; j++)
            cin >> A[i][j];
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int r1, r2;
        int A1[4][4], A2[4][4];
        read(r1, A1);
        read(r2, A2);
        set<int> S;
        for(int i = 0; i < 4; i++)
            S.insert(A1[r1][i]);
        int possibilities = 0, answer;
        for(int i = 0; i < 4; i++){
            if(S.count(A2[r2][i])){
                possibilities++;
                answer = A2[r2][i];
            }
        }
        cout << "Case #" << t << ": ";
        if(possibilities == 0) cout << "Volunteer cheated!\n";
        else if(possibilities == 1) cout << answer << endl;
        else cout << "Bad magician!\n";
    }
}
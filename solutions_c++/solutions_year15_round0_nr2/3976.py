#include <iostream>
#include <fstream>
#include <algorithm>
#define MAX_T 100
#define MAX_D 1000
#define MAX_P 1000
#define INF 2000000000
using namespace std;

ifstream fin ("B-large.in");
ofstream fout ("results.txt");
int T, howManyLifts[MAX_P+1][MAX_P+1];

void init();
void read();
int solve(int D, int P[MAX_D]);
void write(int caseNum, int ans);

int main(){
    init();
    read();
    return 0;
}

void init(){
    for(int i = 2; i <= MAX_P; i++){
        for(int j = i-1; j >= 1; j--){
            if(j >= i/2+i%2) howManyLifts[i][j] = 1;
            else if(j == 1) howManyLifts[i][j] = i-1;
            else{
                howManyLifts[i][j] = howManyLifts[i-j][j] + 1;
            }
        }
    }
}

int solve(int D, int P[MAX_D]){
    sort(P,P+D);
    int tmpAns, ans = INF;
    for(int i = P[D-1]; i >= 1; i--){
        tmpAns = i;
        for(int j = 0; j < D; j++){
            tmpAns += howManyLifts[P[j]][i];
        }
        ans = min(ans,tmpAns);
    }
    return ans;

}

void read(){
    int D, P[MAX_D];
    fin >> T;
    for(int i = 0; i < T; i++){
        fin >> D;
        for(int j = 0; j < D; j++) fin >> P[j];
        write(i,solve(D, P));
    }
    fin.close();
    fout.close();
}

void write(int caseNum, int ans){
    fout << "Case #" << caseNum+1 << ": " << ans << endl;
}

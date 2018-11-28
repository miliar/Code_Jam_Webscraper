#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
int main(){
    ifstream ifs("D-small-attempt0.in");
    ofstream ofs("op_d.txt");
    int test; ifs >> test;
    rep(casenum, test){
        int K, C, S; ifs >> K >> C >> S;
        ofs << "Case #" << casenum + 1 << ": ";
        REP(i, 1, K + 1){
            ofs << i;
            if(i == K) ofs << endl; else ofs << ' ';
        }
    }
    return 0;
}
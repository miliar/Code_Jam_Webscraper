#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
int main(){
    ifstream ifs("A-large.in");
    ofstream ofs("op_a.txt");
    int test; ifs >> test;
    rep(casenum, test){
        string s; ifs >> s;
        int n = s.length();
        string ans = ""; ans += s[0];
        REP(i, 1, n){
            if(ans[0] <= s[i]){
                ans.insert(0, 1, s[i]);
            }else{
                ans += s[i];
            }
        }
        ofs << "Case #" << casenum + 1
            << ": " << ans << endl;
    }
    return 0;
}
 	
/*
 

7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
*/


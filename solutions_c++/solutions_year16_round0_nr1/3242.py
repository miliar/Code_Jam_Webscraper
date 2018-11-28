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
        ll n; ifs >> n;
        if(n == 0){
           ofs << "Case #" << casenum + 1
               << ": " << "INSOMNIA" << endl;
            continue;
        }
        set<int> num;
        ll nn = n;
        while(true){
            ll temp = nn;
            while(temp > 0){
                num.insert((int)(temp % 10));
                temp /= 10;
            }
            if(num.size() == 10) break;
            nn += n;
        }
        ofs << "Case #" << casenum + 1
               << ": " << nn << endl;
    }
    return 0;
}
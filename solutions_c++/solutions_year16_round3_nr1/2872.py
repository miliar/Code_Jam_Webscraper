#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
int n;
int main(){
    ifstream ifs("A-small-attempt0.in");
    ofstream ofs("op_a.txt");
    int test; ifs >> test;
    rep(casenum, test){
        ifs >> n;
        int sum = 0;
        vector<int> pol(n);
        rep(i, n){
            int a;
            ifs >> pol[i];
            sum += pol[i];
        }
        ofs << "Case #" << casenum + 1 << ": ";
        while(sum > 0){
            int ma = -1, x, y;
            int cnt = 0;
            rep(i, n){
                if(ma < pol[i]){
                    ma = pol[i];
                    x = i;
                    y = -1;
                }else if(ma == pol[i]){
                    y = i;
                    cnt++;
                    if(cnt >= 2) y = -1;
                }
            }
            if(y == -1){
                char a = 'A' + x;
                ofs << a;
                pol[x]--;
                sum -= 1;
            }else{
                char a = 'A' + x, b = 'A' + y;
                ofs << a << b;
                pol[x]--; pol[y]--;
                sum -= 2;
            }
            if(sum > 0) ofs << ' ';
        }
        ofs << endl;
    }
    return 0;
}

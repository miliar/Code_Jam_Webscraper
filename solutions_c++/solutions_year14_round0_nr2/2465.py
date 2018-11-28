#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

#define in

typedef long long LL;

#define For(i,b) for(i=0;i<b;i++)
#define Foru(i,a,b) for(i=a;i<=b;i++)
#define Ford(i,a,b) for(i=a;i>=b;i--)
#define mod 1000000007

void solve(){
    int t, i, j, k;
    double c, f, x, ps, pre, nxt, tp, tn, time;
    cin >> t;
    For(i,t){
        ps = 2.0;
        cin >> c >> f >> x;
        //cout << c << ' ' << f << ' ' << x << endl;
        time = 0;
        while(1){
            tp = time + x/ps;
            tn = time + c/ps + x/(ps+f);
            //cout << tp << ' ' << tn << endl;
            if(tp < tn) break;
            time += c/ps;
            ps += f;
        }
        cout << "Case #" << i+1 << ": ";
        printf("%.7f\n",tp);
    }
}
int main(){
    #ifdef in
        freopen("in","r",stdin);
        freopen("out","w",stdout);
    #endif
    solve();
    return 0;
}

#include<stdio.h>
#include<set>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

LL x[2010], y[2010], a[2010], b[5000];
LL n;
int m;

LL P = 1000002013;

set<LL> S;

int main(){
    int ca; scanf("%d",&ca);
    FOE(tt,1,ca){
        scanf("%lld%d",&n,&m);
        LL oc = 0;
        S.clear();
        FOR(i,0,m){
            scanf("%lld%lld%lld",&x[i],&y[i],&a[i]);
            S.insert(x[i]);
            S.insert(y[i]);
            LL ac = ((n + n - (y[i] - x[i] - 1)) * (y[i]-x[i]) / 2) % P * a[i] % P;
            oc = (oc + ac) % P;
        }
        vector<LL> co(S.begin(), S.end());
        CLR(b);
        FOR(i,0,m){
            int x1 = lower_bound(co.begin(), co.end(), x[i]) - co.begin();
            int x2 = lower_bound(co.begin(), co.end(), y[i]) - co.begin();
            FOR(j,x1,x2) b[j] += a[i];
        }

        LL cost = 0;
        while (1){
            int ss=-1, ee=-1;
//            for (int i=0; i<co.size(); i++) printf("%lld ", co[i]); puts("");
//            for (int i=0; i<co.size(); i++) printf("%lld ", b[i]); puts("");
            LL ppl = 1ll<<50;
            FOR(i,0,co.size()){
                if (b[i] > 0){
                    if (ss == -1) ss = i;
                    ee = i;
                    ppl = min(ppl, b[i]);
                } else if (ss != -1){
                    break;
                }
            }
            if (ss == -1) break;
            FOE(i,ss,ee)
                b[i] -= ppl;

            LL len = co[ee+1] - co[ss];
            LL cc = ((n + n-len+1) * len / 2) % P * ppl % P;
            cost = (cost + cc) % P;
        }
//        printf("%lld %lld\n", oc, cost);

        LL ans = (oc - cost + P) % P;
        printf("Case #%d: %lld\n", tt, ans);

    }
    return 0;
}

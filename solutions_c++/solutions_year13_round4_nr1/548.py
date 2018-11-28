#include <cstdio>
#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <stack>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define REP(i,n) for(int64 i=0; i<(int64)n; i++)
typedef long long int64;

#define MAXN 200100
#define MOD 1000002013
int64 x[MAXN],y[MAXN],z[MAXN],n;

int64 fun(int64 x) {
    return (x*n-(x*(x-1))/2)%MOD;
}

int main() {
    int64 nt,m;

    scanf("%lld",&nt);
    REP(ct,nt) {
        int64 tc=0;
        scanf("%lld%lld",&n,&m);
        REP(i,m) {
            scanf("%lld %lld %lld",&x[i],&y[i],&z[i]);
            tc += z[i]*fun(y[i]-x[i]);
            tc %= MOD;
        }

        while (1) {
            int mxc=0,mi,mj;
            REP(i,m)
                REP(j,m)
                    if (i!=j && x[i]<x[j] && y[i]<y[j] &&
                        max(x[i],x[j])<=min(y[i],y[j])) {
                        int mxp=min(z[i],z[j]);
                        if (mxp>mxc) {
                            mxc=mxp;
                            mi=i; mj=j;
                        }
                    }

            int64 tc2=0;
            REP(i,m) {
                tc2 += z[i]*fun(y[i]-x[i]);
            }
            z[mi]-=mxc;
            z[mj]-=mxc;
            x[m]=x[mi]; y[m]=y[mj]; z[m++]=mxc;
            x[m]=x[mj]; y[m]=y[mi]; z[m++]=mxc;
            int64 tc3=0;
            REP(i,m) {
                tc3 += z[i]*fun(y[i]-x[i]);
            }
            if (tc2==tc3) break;
        }

        int64 tc2=0;
        REP(i,m) {
            tc2 += z[i]*fun(y[i]-x[i]);
        }

        printf("Case #%lld: %lld\n",ct+1, ((tc-tc2)%MOD+MOD)%MOD);
    }
    return 0;
}

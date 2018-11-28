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
#define INF 0x3f3f3f3f
#define REP(i,n) for(int i=0; i<n; i++)
typedef long long int64;

int main() {
    int nt;

    scanf("%d",&nt);
    REP(ct,nt) {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);

        double rt=2, t=0;
        double res=1e100;
        REP(i,(int)x) {
            res=min(res,t+x/rt);
            t+=c/rt;
            rt+=f;
        }
        printf("Case #%d: %.7lf\n",ct+1,res);
    }
    return 0;
}


#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#define pb push_back
#define mp make_pair
using namespace std;
typedef long long ll;
const int inf = 0x3f3f3f3f;
const double eps = 1e-9;
int n;
double v,x;
double R[2],C[2];
int main()
{
    freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1; cas<=T; cas++)
    {
        scanf("%d%lf%lf",&n,&v,&x);
        for(int i=0; i<n; i++) scanf("%lf%lf",&R[i],&C[i]);
        printf("Case #%d: ",cas);
        if(n == 1)
        {
            if(fabs(C[0]-x) < eps)
            {
                printf("%.10lf\n",v/R[0]);
            }
            else puts("IMPOSSIBLE");
        }
        else
        {
            if(x-C[0]>eps && x-C[1]>eps || C[0]-x>eps && C[1]-x>eps)
            {
                puts("IMPOSSIBLE");
                continue;
            }
            double ans = 1e12;
            if(fabs(C[0]-x) < eps)
            {
                ans = min(ans,v/R[0]);
            }
            if(fabs(C[1]-x) < eps)
            {
                ans = min(ans,v/R[1]);
            }
            if(fabs(C[0]-C[1])>eps)
            {
                double v0 = (C[1]-x)/(C[1]-C[0])*v;
                double v1 = v-v0;
                if(v1 >= 0 && v0 >= 0)
                {

                    ans = min(ans,max(v1/R[1],v0/R[0]));
                }
            }
            else
            {
                ans = min(ans,v/(R[0]+R[1]));
            }
            if(ans < 1e11) printf("%.10lf\n",ans);
            else puts("IMPOSSIBLE");
        }
    }
    return 0;
}

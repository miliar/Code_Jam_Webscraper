#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<set>
#include<iostream>

using namespace std;

typedef long long ll;
const double eps=1e-10;

int n;
double r[1005],c[1005],vv,xx;

void solve()
{
    if(n==1)
    {
        if(fabs(xx-c[0])>eps) {printf("IMPOSSIBLE\n");}
        else
        {
            printf("%.8lf\n",vv/r[0]);
        }
    }
    else if(n==2)
    {
        if(c[0]>c[1]) {swap(c[0],c[1]);swap(r[0],r[1]);}
        if(c[1]+eps<xx||xx<c[0]-eps) {printf("IMPOSSIBLE\n");}
        else
        {
            if(fabs(c[1]-c[0])<eps) printf("%.8lf\n",vv/(r[0]+r[1]));
            else
            {
                double tt=(xx-c[0])*vv/r[1]/(c[1]-c[0]);
                tt=max(tt,(vv-r[1]*tt)/r[0]);
                printf("%.8lf\n",tt);
            }
        }
    }
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T,I=1,i,j;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d %lf %lf",&n,&vv,&xx);
        for(i=0;i<n;i++) scanf("%lf %lf",r+i,c+i);
        printf("Case #%d: ",I++);
        solve();
    }
    return 0;
}

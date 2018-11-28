#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
using namespace std;
#define Rep(i,n) for (int i=0;i<(n);i++)
#define For(i,l,r) for (int i=(l);i<=(r);i++)
#define PB push_back
#define MP make_pair
#define N 1005
#define oo 1e100
#define eps 1e-8
int T,n;
double V,X,ans,t1,t2;
double R[1005],C[1005];

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small1.out","w",stdout);

    scanf("%d",&T);
    For(Case,1,T)
    {
        scanf("%d%lf%lf",&n,&V,&X);
        for (int i=0;i<n;i++)
            scanf("%lf%lf",&R[i],&C[i]);

        printf("Case #%d: ",Case);

        ans=oo;

        if (n==1)
        {
            if (fabs(X-C[0])<eps)
                printf("%.8f\n",V/R[0]);
            else puts("IMPOSSIBLE");
        } else
        {
            Rep(i,n)
            {
                if (fabs(X-C[i])<eps)
                    ans=min(ans,V/R[i]);
            }
            if ((fabs(X-C[0])<eps)&&(fabs(X-C[1])<eps))
                ans=min(ans,V/(R[0]+R[1]));

            if (ans<oo)
            {
                printf("%.8f\n",ans);
                continue;
            }
            if ((X-C[0]<0)==(X-C[1]<0))
            {
                puts("IMPOSSIBLE");
                continue;
            }

            if (fabs(C[0]-C[1])<eps)
                printf("%.8f\n",V/(R[0]+R[1]));
            else
            {
                t1=(C[0]-X)*V/(C[0]-C[1])/R[1];
                t2=(C[1]-X)*V/(C[1]-C[0])/R[0];
                printf("%.8f\n",max(t1,t2));
            }
        }
    }



    return 0;
}

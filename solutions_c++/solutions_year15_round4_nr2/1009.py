#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<deque>
#pragma comment(linker, "/STACK:1024000000,1024000000")
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define maxn 11005
#define mod 1000000007
#define FI first
#define SE second
double a[15];
double b[15];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int n;
        scanf("%d",&n);
        double A,T;
        scanf("%lf%lf",&A,&T);
        for(int i=1;i<=n;i++)   scanf("%lf%lf",a+i,b+i);
        printf("Case #%d: ",cas);
        if(n==1)
        {
            if(T!=b[1]) printf("IMPOSSIBLE\n");
            else printf("%.10f\n",A/a[1]);
        }
        else
        {
            if (max(b[1],b[2]) < T || min(b[1],b[2]) > T)
            {
                printf("IMPOSSIBLE\n") ;
                continue;
            }
            if(b[1]==b[2])
            {
                if(T==b[1]) printf("%.10f\n",A/(a[1]+a[2]));
                else printf("IMPOSSIBLE\n");
                continue;
            }
            double x2=(A*T-b[1]*A)/(a[2]*b[2]-a[2]*b[1]);
            double x1=(A-x2*a[2])/a[1];
            printf("%.10f\n",max(x1,x2));
        }
    }
}

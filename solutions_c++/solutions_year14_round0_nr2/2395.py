#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define maxn 200000
#define INF 100000000
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
using namespace std;
double C,F,X,a[maxn];
int main()
{
    int tt;
    scanf("%d",&tt);
    int cot=1;
    while(tt--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        a[0]=0;
        for(int i=1;i<200000;i++)
            a[i]=a[i-1]+C/(2+(i-1)*F);
        double ans=X/2;
        for(int i=0;i<200000;i++)
            ans=min(ans,a[i]+X/(2+i*F));
        printf("Case #%d: %.7f\n",cot++,ans);
    }
}

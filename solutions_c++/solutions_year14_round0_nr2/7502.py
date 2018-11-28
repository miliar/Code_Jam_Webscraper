#include<cstdio>
#include<cstring>
#include<limits.h>
#define eps 1e-10
int T;
double C,F,X;

bool ok(int mid)
{
    double t1 = X/(2.0 + (double)mid*F);
    double t2 = C/(2.0 + (double)mid*F) + X/(2.0 + (double)(mid+1)*F);
    //printf("t1 = %.7lf\n",t1);
    //printf("t2 = %.7lf\n",t2);
    if(t1 < t2)return true;
    else return false;
}

void solve()
{
    if(X/2. < C/2. + X/(2. + F))
    {
        printf("%.7lf\n",X/2.);
        return;
    }

    int lb = 0, ub = INT_MAX;
    while(ub - lb > 1)
    {
        int mid = (lb + ub)/2;
        if(ok(mid))ub = mid;
        else lb = mid;
    }
    //printf("lb = %d,ub = %d\n",lb,ub);
    int tot = lb + 1;
    //printf("tot = %d\n",tot);
    double ans = 0.0;
    for(int i = 0;i < tot;i++)
    {
        ans += C/(2.0 + i*F);
        //printf("%.7lf\n",ans);
    }
    ans += X/(2.0 + tot*F);
    printf("%.7lf\n",ans);
    return;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(int cases = 1;cases <= T;cases++)
    {
        printf("Case #%d: ",cases);
        scanf("%lf %lf %lf",&C,&F,&X);
        //printf("%lf %lf %lf\n",C,F,X);
        solve();
    }
    return 0;
}

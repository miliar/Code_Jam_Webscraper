#include<cstdio>
#include<algorithm>

using namespace std;

double C,F,X,T,ans,R;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for ( int x=1 ; x<=t ; x++ )
    {
        scanf("%lf%lf%lf",&C,&F,&X);
        T = 0;
        R = 2;
        ans = X/R;
        while ( T <= ans )
        {
            T += C/R;
            R += F;
            ans = min ( ans , T + X/R);
        }
        printf("Case #%d: %.7lf\n",x,ans);
    }
}

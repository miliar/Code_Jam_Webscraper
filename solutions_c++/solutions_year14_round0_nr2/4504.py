#include <cstdio>
#include<algorithm>
using namespace std;

int main()
{
//    freopen("B-large.in","r",stdin);

    int T;
    double c,f,x,ans,temp;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/2.0;
        temp=c/2.0;
        for(int i=1;i<=100000;i++)
        {
            ans=min(ans,temp+x/(2.0+i*f));
            temp+=c/(2.0+i*f);
        }
        printf("Case #%d: %.7lf\n",kase,ans);
    }
    return 0;
}

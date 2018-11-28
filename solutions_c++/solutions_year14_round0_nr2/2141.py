#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t;
    double c,f,x;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        /*double pc=2,ans=0;
        while(true)
        {
            ans+=c/pc;
            if((x-c)*f<=c*pc)
            {
                ans+=(x-c)/pc;
                break;
            }
            pc+=f;
        }*/
        double ans=0;
        int k=ceil(x/c-1-2/f);
        if(k<0)
            k=0;
        for(int i=0; i<k; ++i)
            ans+=1/(2+i*f);
        ans*=c;
        ans+=x/(2+k*f);
        printf("Case #%d: %.7f\n",cas,ans);
    }
}

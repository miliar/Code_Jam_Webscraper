#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    freopen("intput.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,i,loc;
    double c,f,x,sum1,sum2,t,ans,x1,ans1,ans2;
    int k=0;
    scanf("%d",&T);
    while(T--)
    {
        sum1=0.0;
        sum2=0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        for(i=0;i<=2000;i++)
        {
            x1=i*1.0;
            if(i==0)
            sum1=0.0;
            else
            sum1+=c/(2+f*(x1-1.0));
            sum2+=c/(2+f*x1);
            ans1=sum1+x/(2+f*x1);
            ans2=sum2+x/(2+f*(x1+1));
           // printf("ans1:%lf ans2:%lf\n",ans1,ans2);
            //printf("%lf\n",ans);
            if((ans1-ans2)<0)
            {
                break;
            }
        }
         ans=x/(2+f*(x1*1.0))+sum1;
        printf("Case #%d: %.7lf\n",++k,ans);
    }
    return 0;
}

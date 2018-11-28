#include<cstdio>
using namespace std;
double c,f,x;
void solve()
{
    double time=0,income=2.0,y1,y2;
    double eps=0.00000001;
    while(1)
    {
        y1=x/income;
        y2=c/income;
        y2+=x/(income+f);
        if(y1+eps<y2)
        {
            time+=x/income;
            break;
        }
        else
        {
            time+=c/income;
            income+=f;
        }
    }
    printf("%.7lf\n",time);
}
int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        printf("Case #%d: ",i);
        solve();
    }
}

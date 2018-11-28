#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    double c,f,x;
    int t,cs;
    //freopen("C:\\Users\\Utkarsh\\Desktop\\test.in","r",stdin);
    //freopen("C:\\Users\\Utkarsh\\Desktop\\output.txt","w",stdout);
    scanf("%d",&t);
    for(cs=1;cs<=t;cs++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        double r=2.0,time=0.0;
            while(1)
            {
                double a,b,m;
                a=x/r;
                b=c/r;
                m=x/(r+f);
                if(a>b+m)
                {
                    time+=c/r;
                    r+=f;
                }
                else
                {
                   break;
                }
            }
            time+=x/r;
        printf("Case #%d: %.7lf\n",cs,time);
    }
    return 0;
}

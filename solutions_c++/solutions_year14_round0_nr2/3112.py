#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("c:\\temp\\in.txt","r",stdin);
    freopen("c:\\temp\\output.txt","w",stdout);
    int test_case;
    scanf("%d",&test_case);
    for(int ca=1;ca<=test_case;ca++)
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double time=0;
        double temp=x;
        double per_second=2.0;
       double min_second=x/2.0;
        while(1)
        {
           time=time+(c/per_second);
           per_second=per_second+f;
           double t=(x/per_second);
           t=t+time;
           if(min_second>=t)
            min_second=t;
           else break;
        }
       printf("Case #%d: %.7lf\n",ca,min_second);
    }
    return 0;
}

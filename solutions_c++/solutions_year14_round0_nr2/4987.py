#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int t,k;
    double n,m,a;
    scanf("%d",&t);
    for(k=1; k<=t; k++)
    {
        scanf("%lf%lf%lf",&n,&a,&m);
        double s=2;
        double ans=0;
        while(1)
        {
            double num=n/s+m/(s+a);
            if(num>(m/s))
            {
                ans+=m/s;
                break;
            }
            ans+=n/s;
            s+=a;
        }
        printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}

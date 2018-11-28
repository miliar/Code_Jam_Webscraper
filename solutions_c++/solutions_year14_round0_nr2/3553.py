#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;
int main(void)
{
    freopen("B-large.in" , "r" ,stdin);
    freopen("laobi.out" , "w" , stdout);
    int casenum;
    scanf("%d",&casenum);
    for(int k=1;k<=casenum;k++)
    {
        double c,f,x;
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=0.0;
        double sudu=2.0;
        biaohao:
        double a=x/sudu;
        double b=c/sudu;
        if(x/(sudu+f)+b<a)
        {
            sudu=sudu+f;
            ans=ans+b;
            goto biaohao;
        }
        ans=ans+a;
        printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}

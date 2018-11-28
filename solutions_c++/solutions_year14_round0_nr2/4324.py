#include <iostream>
#include<stdio.h>

using namespace std;

void cookie(int t);
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
            cookie(i);
    return 0;
}
void cookie(int a)
{
    double c,f,x;
    double t,m1,m2;
    double bt,pt;
    t=0.0;
    scanf("%lf%lf%lf",&c,&f,&x);
    double pr=2.0;
    m1=x/pr;
    while(1)
    {
        bt=c/pr;
        t=t+bt;
        pr=pr+f;
        pt=x/pr;
        m2=pt+t;
        if(m1<m2)
            break;
        else
        {
            m1=m2;
        }
    }
    printf("Case #%d: %0.7f\n",++a,m1);
}

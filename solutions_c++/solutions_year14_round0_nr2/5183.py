#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    int t,ct=1;
    scanf("%d",&t);

    while(t--)
    {
        long double c,f,x,r,tt,cc=0.0;
        scanf("%Lf%Lf%Lf",&c,&f,&x);
        r=2.0;
        tt=0.0;
        while(x/r>c/r+x/(r+f))
        {
            tt=tt+c/r;
            r=r+f;
        }
        tt=tt+(x-cc)/r;
        printf("Case #%d: %.7Lf\n",ct,tt);
        ct++;
    }
    return 0;
}

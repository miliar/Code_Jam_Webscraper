#include<stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<cmath>
#include<ctype.h>
#define LL unsigned long long
#define h1t35h using
#define rocks namespace
#define theworld std;
#define SI(n) scanf("%d",&n);
#define SF(n) scanf("%lf",&n);
#define SLL(n) scanf("%lld",&n);
#define SC(n) scanf("%c",&n);
#define PC(n) printf("%c",&n);
#define PI(n) printf("%d",n);
#define PF(n) printf("%f",n);
#define PLL(n) printf("%lld",n);
#define FOR(x,n) for(x=0;x<(n);x++)
#define FORL(x,a,b) for(x=a;x<b;x++)
LL gcd(LL a, LL b)
{
    return b?gcd(b,a%b):a;
}
h1t35h rocks theworld;
int main()
{
    register int loop,test,i,j;
    freopen("B-large.in","r",stdin);
    //freopen("B.out","r",stdout);
    SI(test);
    loop=0;
    double c,f,x;
    while(loop<test)
    {
            SF(c)
            SF(f)
            SF(x)
            double n;
            n=(double)((x/c)-(2/f)-1);
            double val;
            if(n<0)
            n=0;
            n=(double)ceil(n);
            val=0;
            FOR(i,n)
            {
                val+=(double)c/(2+(i*f));
//                cout<<c/(2+(i*f))<<" ";
            }
//            cout<<endl;
            val+=(double)x/(2+n*f);
//            cout<<"Add: "<<x/(2+n*f)<<endl;
            printf("Case #%d: %0.7lf\n",loop+1,val);
//            cout<<"Case #"<<loop+1<<": "<<val<<endl;

            loop++;
    }
    return 0;
}


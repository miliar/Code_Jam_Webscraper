#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
long long t;
double c,f,x,s,ans;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("answer.txt","w",stdout);
    scanf("%lld",&t);
    for(int o=1; o<=t; o++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        s=2;
        ans=0;
        while(1)
        {
            if(x/s<c/s+x/(s+f)) {ans+=x/s; break;}
            else {ans+=c/s; s+=f;}
        }
        printf("Case #%d: %.7lf\n",o,ans);
    }
    return 0;
}

#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int T,C;
double c,f,x,s,ans;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for (C=1;C<=T;C++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);    
        s=2.0; ans=0.0;
        while (s*c<f*(x-c))
        {
            ans+=c/s;
            s+=f;
        }
        ans+=x/s;
        printf("Case #%d: %.7f\n",C,ans);
    }
    
    
    return 0;    
}

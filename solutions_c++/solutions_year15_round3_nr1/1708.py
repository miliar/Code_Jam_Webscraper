//#include<stdio.h>
//#include<stdlib.h>
//#include<string.h>
#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
int main()
{
    int t,r,c,w,i,j;
    sd(t);
    for(i=1;i<=t;i++)
    {
        sd(r);
        sd(c);
        sd(w);
        j=c/w;
        if(c%w==0)
            j--;
        j+=w;
        printf("Case #%d: %d\n",i,j);
    }
    return 0;
}

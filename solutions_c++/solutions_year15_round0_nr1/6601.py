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
    int t,n,i,j,k,l,s;
    char a[10];
    sd(t);
    for(l=1;l<=t;l++)
    {
        sd(n);
        ss(a);
        s=(int)a[0]-48;k=0;
        for(i=1;i<=n;i++)
        {
            j=(int)a[i]-48;
            if(s<i&&j!=0)
            {
                k+=i-s;
                s+=i-s;
            }
            s+=j;
        }
        printf("Case #%d: %d\n",l,k);
    }
    return 0;
}

#include<cstdio>
#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<cstring>
using namespace std;
bool ok(char *str)
{
    int n=strlen(str);
    for(int i=0;i<n/2;i++)
    {
        if(str[i]!=str[n-1-i])
            return false;
    }
    return true;
}
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    __int64 a,b,i,k;
    char ss[20];
    int ncase,j=1;
    scanf("%d",&ncase);
    while(ncase--)
    {
        scanf("%I64d%I64d",&a,&b);
        k=0;
        __int64 m=(__int64)sqrt(a);
        for(i=m;i*i<=b;i++)
        {
            sprintf(ss,"%I64d",i*i);
            if(!ok(ss)) continue;
            sprintf(ss,"%I64d",i);
            if(!ok(ss)) continue;
            if(i*i>=a) k++;
        }
        printf("Case #%d: ",j++);
        printf("%I64d\n",k);
    }
    return 0;
}

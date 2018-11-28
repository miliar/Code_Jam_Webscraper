#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
using namespace std;
bool judge(int x)
{
    int stk[10],top=0,i;
    while(x)
    {
        stk[top++]=x%10;
        x/=10;
    }
    for(i=0;i<top/2;i++)
    {
        if(stk[i]!=stk[top-i-1])return 0;
    }
    return 1;
}
bool f(int x)
{
    if(judge(x)==0)return 0;
    int sq=sqrt(x);
    if(sq*sq==x)
    {
        if(judge(sq))return 1;
    }
    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas,ca=0,i;
    scanf("%d",&cas);
    while(cas--)
    {
        printf("Case #%d: ",++ca);
        int A;
        int B;
        int cnt=0;
        scanf("%d%d",&A,&B);
        for(i=A;i<=B;i++)
        {
            if(f(i))cnt++;
        }
        printf("%d\n",cnt);
    }
    return 0;
}

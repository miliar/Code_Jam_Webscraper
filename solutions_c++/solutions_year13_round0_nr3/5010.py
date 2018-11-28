#include<iostream>
#include<cstdio>
#include<cmath>
 
using namespace std;
 
int a[40]=

{1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
 
int b[10000001]={0};
int c[10000001]={0};
 
int main()
{
    int i,ginti=0,t,k=1,sa,sb,jawab=0;
    long long int aa,bb;
    for(i=0;i<39;i++)
    {
        b[a[i]]=1;
    }
    
    for(i=0;i<10000001;i++)
    {
        ginti=ginti+b[i];
        c[i]=ginti;
    }
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%lld%lld",&aa,&bb);
        sa=ceil(sqrt(aa));
        sb=floor(sqrt(bb));
        jawab=c[sb]-c[sa];
        if(b[sa])
        jawab++;
        printf("Case #%d: %d\n",k,jawab);
    }
    return 0;
}    
#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#define MAX 10000000
typedef long long int ll;
using namespace std;
ll a[10000];
int pallin(ll num)
{
    ll i,temp=0;
    i=num;
    while(i)
    {
        temp=(temp*10)+(i%10);
        i/=10;
    }
    if(temp==num)return 1;
    return 0;
}
int main()
{
    int t;
    freopen("C-large-1.in","r",stdin);
    freopen("output1.txt","w",stdout);
    ll i,j,counter=0;
    a[0]=1;
    for(i=2; i<=MAX; i++)
    {
        j=i*i;
        if(pallin(i))
        if(pallin(j))
        a[++counter]=j;
    }
    scanf("%d",&t);
    ll A,B;
    int indexa,indexb,ans=0,count2=0;
    while(t--)
    {
        count2++;
        ans=0;
        scanf("%lld%lld",&A,&B);
        for(i=0;i<=counter;i++)
        if((a[i]>=A)&&(a[i]<=B))ans++;
        printf("Case #%d: %d\n",count2,ans);
    }
    return 0;
}

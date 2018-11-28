#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include <fstream>
using namespace std;
const int mod = 1e9+7;
#define LL long long
#define mem(a,b) memset(a,b,sizeof(a))
int ans[1005];
int f(int x)
{
    int a[10],t=0,i,j;
    while(x)
    {
        a[t++]=x%10;
        x/=10;
    }
    if(t==1)return 1;
    int d=t/2;
    //cout<<d<<"((("<<endl;
    for(i=0;i<t/2;i++)
    {
        j=t-i-1;
        if(a[i]!=a[j])return 0;
    }
    return 1;
}
int main()
{
    int i,j,t,a,b,g=0;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    for(i=1;i<=100;i++)
    {
        if(i*i<=1000&&f(i*i)&&f(i))
        {
            ans[g++]=i*i;
        }
    }
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
        scanf("%d%d",&a,&b);
        int sum=0;
        for(i=0;i<g;i++)
        {
            if(ans[i]>=a&&ans[i]<=b)sum++;
        }
        printf("Case #%d: %d\n",++cas,sum);
    }
}

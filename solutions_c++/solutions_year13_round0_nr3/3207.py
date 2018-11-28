#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
int num[100];
vector<int>vt;
int get(long long x)
{
    int d=0;
    while(x)num[d++]=x%10,x/=10;
    for(int i=0;i<d;++i)
        if(num[i]!=num[d-i-1])return 0;
    return 1;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    for(long long i=1;i<=10000000;++i)
    {
        if(get(i)&&get(i*i))vt.push_back(i*i);
    }
    int t,Case=0;
    scanf("%d",&t);
    while(t--)
    {
        long long n,m;
        scanf("%lld%lld",&n,&m);
        int sum=0;
        for(int i=0;i<vt.size();++i)
        if(vt[i]>=n&&vt[i]<=m)++sum;
        printf("Case #%d: %d\n",++Case,sum);
    }
    return 0;
}

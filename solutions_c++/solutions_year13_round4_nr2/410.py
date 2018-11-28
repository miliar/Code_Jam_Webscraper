#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
using namespace std;
#define DEBUG 0
#define debug(x) if(DEBUG)cout<<#x<<": "<<x<<endl;
#define FOR(i,j,k) for(i=j;i<=k;++i)
#define REP(i,j) for(i=0;i<j;++i)
#define FORD(i,j,k) for(i=j;i>=k;--i)
#define met(i,j) memset(i,j,sizeof(i))
#define sz(i) ((int)i.size())
#define PB push_back
#define MK make_pair
#define IOopen ios_base::sync_with_stdio(0)
const int inf=~0U>>1;
typedef pair<int, int> PII;
typedef unsigned long long ULL;
typedef long long LL;
LL n,p,m;

bool check1(LL i)
{
    LL small,t1,j;
    small=i;t1=0;
    FORD(j,n-1,0)
    {
        if(small>0)
        {
            small=(small-1)/2;
        }else
        {
            t1+=1LL<<j;
        }
    }
    return m-t1<=p;
}

bool check2(LL i)
{
    LL large,t2,j;
    large=m-i-1;t2=0;
    FORD(j,n-1,0)
    {
        if(large>0)
        {
            t2+=1LL<<j;
            large=(large-1)/2;
        }
    }
    return m-t2<=p;
}

void work()
{
    LL i,j,k,ans1,ans2;
    cin>>n>>p;
    m=1LL<<n;
    i=0;j=m;
    while(i<j)
    {
        k=(i+j)/2;
        if(check1(k))i=k+1;else j=k;
    }
    ans1=i-1;
    i=0;j=m;
    while(i<j)
    {
        k=(i+j)/2;
        if(check2(k))i=k+1;else j=k;
    }
    ans2=i-1;
    cout<<ans1<<" "<<ans2<<endl;
}

int main()
{
    int i,T;
    scanf("%d",&T);
    FOR(i,1,T)
    {
        printf("Case #%d: ",i);
        work();
    }
}

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
#define N 10000005
ULL old,now;
int n,m;
int s[N],t[N],p[N];

void init()
{
    int i;
    now=old=0;
    scanf("%d%d",&n,&m);
    FOR(i,1,m)
    {
        scanf("%d%d%d",&s[i],&t[i],&p[i]);
        old+=(ULL(n)*(t[i]-s[i])-ULL(t[i]-s[i])*ULL(t[i]-s[i]-1)/2ULL)*ULL(p[i]);
    }
}

void work()
{
    int bj,i,j;
    while(1)
    {
        bj=0;
        FOR(i,1,m)
        {
            FOR(j,1,m)
            {
                if(s[i]<s[j] && t[i]>=s[j] && t[i]<t[j])
                {
                    bj=1;
                    if(abs(p[i]-p[j])==0)
                    {
                        swap(t[i],t[j]);
                    }else
                    {
                        if(p[i]>p[j])
                        {
                            s[++m]=s[i];
                            t[m]=t[i];
                            p[m]=p[i]-p[j];
                            p[i]=p[j];
                        }else
                        {
                            s[++m]=s[j];
                            t[m]=t[j];
                            p[m]=p[j]-p[i];
                            p[j]=p[i];
                        }
                        swap(t[i],t[j]);
                    }
                }
            }
        }
        if(!bj)break;
    }
    FOR(i,1,m)
    {
        now+=(ULL(n)*(t[i]-s[i])-ULL(t[i]-s[i])*ULL(t[i]-s[i]-1)/2ULL)*ULL(p[i]);
    }
    cout<<old-now<<endl;
}

int main()
{
    int i,T;
    cin>>T;
    FOR(i,1,T)
    {
        printf("Case #%d ",i);
        init();
        work();
    }
}

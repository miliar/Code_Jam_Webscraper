#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>
#define MOD 1000000007
using namespace std;
int visit[6],visit1[6];
int main()
{
    int t,n,ctr=0,a1,a2,num;
    freopen("jam14i.txt","r",stdin);
    freopen("jam14o.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        ctr++;
        scanf("%d",&a1);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&num);
                if(i==a1)
                    visit[j]=num;
            }
        }
        scanf("%d",&a2);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&num);
                if(i==a2)
                    visit1[j]=num;
            }
        }

        int ans=-1;
        int f=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(visit[i]==visit1[j] && ans==-1)
                {
                    ans=visit[i];
                }
                else if (visit[i]==visit1[j])
                {
                    f=1;
                }
            }
        }

        cout<<"Case #"<<ctr<<": ";
        if(f==1)
            cout<<"Bad magician!\n";
        else if(ans==-1)
            cout<<"Volunteer cheated!\n";
        else
            cout<<ans<<"\n";

    }
    return 0;
}

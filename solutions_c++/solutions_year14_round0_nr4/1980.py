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
double ar[1003],ar1[1003];
int main()
{
    int t,n,ctr=0;
    freopen("jam14i.txt","r",stdin);
    freopen("jam14o.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        ctr++;
        for(int i=0;i<n;i++)
        {
            scanf("%lf",&ar[i]);
        }
        for(int i=0;i<n;i++)
        {
            scanf("%lf",&ar1[i]);
        }
        sort(ar,ar+n);
        sort(ar1,ar1+n);
        int iter=0;
        int naomiactual=0;
        int naomiwicked=n;
        int j;
        /*for(int i=0;i<n;i++)
        {
            cout<<ar[i]<<" ";
        }
        cout<<"\n";
        for(int i=0;i<n;i++)
        {
            cout<<ar1[i]<<" ";
        }
        cout<<"\n";
        */
        for(int i=0;i<n;i++)
        {
            for(j=iter;j<n;j++)
            {
                if(ar1[j]>ar[i])
                {
                    iter=j+1;
                    break;
                }
            }
            if(j==n)
            {
                naomiactual++;
            }
        }
        j=n-1;
        int i=0;
        int j1=n-1;
        while(i<=j && j1>=0)
        {
            if(ar[j]>ar1[j1])
            {
                j--;
                j1--;
            }
            else if(ar[i]<ar1[j1])
            {
                i++;
                j1--;
                naomiwicked--;
            }
            else
            {
                break;
            }
        }
        cout<<"Case #"<<ctr<<": "<<naomiwicked<<" "<<naomiactual<<"\n";
    }
    return 0;
}

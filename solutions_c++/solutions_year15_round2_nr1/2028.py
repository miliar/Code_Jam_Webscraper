#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#define PII pair<int,int>
#define ff first
#define ss second
#define VI vector<int>
#define LL long long
#define MP make_pair
#define LD long double
#define PB push_back
#define ALL(V) V.begin(),V.end()
#define abs(x) max((x),-(x))
#define PDD pair<LD,LD>
#define VPII vector< PII >
#define siz(V) ((int)V.size())
#define FOR(x, b, e)  for(int x=b;x<=(e);x++)
#define FORD(x, b, e) for(int x=b;x>=(e);x--)
#define REP(x, n)     for(int x=0;x<(n);x++)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
using namespace std;

const int MAXN=1e6+5;
int odl[MAXN];
int t, n, a;

int revers (int b)
{
    int x=0;
    while(b>0)
    {
        x+=(b%10);
        b/=10;
        x*=10;
    }
    x/=10;
    return x;
}

int main()
{
    odl[1]=1;
    fill(odl+2, odl+1000002, 1000003);
    for(int i=1;i<=999999;i++)
    {
        odl[i+1]=min(odl[i+1], odl[i]+1);
        if(revers(i)>i)
            odl[revers(i)]=min(odl[revers(i)], odl[i]+1);
    }
    scanf("%d", &t);
    while(t--)
    {
        a++;
        scanf("%d", &n);
        printf("Case #%d: ", a);
        printf("%d\n", odl[n]);
    }
    return 0;
}

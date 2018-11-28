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
#include <sstream>

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream SS;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) MAX(a,-(a))

#define SS(a) scanf("%d",&a)
#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define MOD 1000000007
#define INF (1<<31)

int a[101][101];
int n,m;
bool check()
{
    REP(i,n)
    {
        REP(j,m)
        {
            int cur = a[i][j];
            bool flag1 = true;
            bool flag2 = true;
            REP(k,n)
            {
                if (cur < a[k][j])
                {
                    flag1 = false;
                    break;
                }
            }
            REP(k,m)
            {
                if (cur < a[i][k])
                {
                    flag2 = false;
                    break;
                }
            }

            if (!flag1 && !flag2)
            {
                return 0;
            }

        }
    }
    return 1;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b1.out","w",stdout);
    int t;
    cin>>t;
    FOR(tt,1,t)
    {
        cin>>n>>m;
        REP(i,n) REP(j,m) cin>>a[i][j];
        printf("Case #%d: ",tt);
        if (check()){
            cout<<"YES\n";
        } else cout<<"NO\n";
    }
    return 0;
}

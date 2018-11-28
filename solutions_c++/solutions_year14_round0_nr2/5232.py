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
#include<limits>
using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream SS;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) MAX(a,-(a))

#define ss(a) scanf("%d",&a)
#define SZ(a) ((int)a.size())
#define pb(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define MOD 1000000007
#define INF (1<<31)

#define EPS 1e-12
void solve(int );
int main()
{
    int n;
    ss(n);
    REP(i,n)
    {
        solve(i+1);
    }
    return 0;
}
void solve(int k)
{
    double c,f,x;
    cin>>c>>f>>x;
    double current_rate=2;
    double previous_cost=0;
    double current_cost=0;
    double min=numeric_limits<double>::max();
    while(1)
    {
        current_cost=previous_cost+x/current_rate;
        if(current_cost<min)
        {
            min=current_cost;
        }
        else
        {
            break;
        }
        previous_cost+=c/current_rate;
        current_rate+=f;

    }
    printf("Case #%d: %.7lf\n",k,min);

}

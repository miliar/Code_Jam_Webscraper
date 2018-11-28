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
vector <double> vec1;
vector <double> vec2;
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
    int n;
    double a;
    ss(n);
    REP(i,n)
    {
        scanf("%lf",&a);
        vec1.pb(a);
    }

    REP(i,n)
    {
        scanf("%lf",&a);
        vec2.pb(a);
    }
    sort(vec1.begin(),vec1.end());
    sort(vec2.begin(),vec2.end());

    int ans1=0;
    int ans2=0;
    int pos=0;
    int j=0;
    int t=0;
    REP(i,n)
    {
        j=pos;
        t=0;
        for(j=pos;j<n;j++)
        {
            if(vec2[j]>vec1[i])
            {
                t=1;
                pos=j+1;
                break;
            }
        }
        if(t==0)
        {
            ans1=n-i;
            break;
        }
    }
    double max1=vec1[n-1];
    double max2=vec2[n-1];
    int s=n-1;
    int q=n-1;
    REP(i,n)
    {
    	if(vec1[s]>vec2[q])
    	{
    		ans2++;
    		s--;
    		q--;
    		}
    		else
    		{
    			q--;
    			}
    			}
    vec1.clear();
    vec2.clear();
    printf("Case #%d: %d %d\n",k,ans2,ans1);

}

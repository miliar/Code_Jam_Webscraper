#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>

using namespace std;


typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define REV(i,a,b) for(int i=a-1;i>=b;i--)
#define rev(i,n) REV(i,n,0)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define GI ({ int x; scanf("%d",&x); x; })
#define GLL ({ LL x; scanf("%lld",&x); x; })
#define ALL(v) v.begin(),v.end()
#define PB push_back
#define MP make_pair
#define PQ priority_queue
#define inf (int)(1e9)
#define linf (LL)(1e18)
#define eps (double)(1e-9)
#define leps (LD)(1e-18)
#define PI (double)(3.141592653589793238)


int n;
double a[1005],b[1005];

int dwar()
{
	set<double> s;
	rep(i,n)
		s.insert(a[i]);
	int ans=0;
	rep(i,n)
	{
		double curr=(s.upper_bound(b[i])==s.end()?*s.begin():*s.upper_bound(b[i]));
		s.erase(curr);
		ans+=(curr>b[i]);
	}
	return ans;
}

int war()
{
	set<double> s;
	rep(i,n)
		s.insert(b[i]);
	int ans=0;
	rep(i,n)
	{
		double curr=(s.upper_bound(a[i])==s.end()?*s.begin():*s.upper_bound(a[i]));
		s.erase(curr);
		ans+=(curr<a[i]);
	}
	return ans;
}

void solve(int t)
{
	cin>>n;
	rep(i,n)
		cin>>a[i];
	rep(i,n)
		cin>>b[i];
	cout<<"Case #"<<t<<": "<<dwar()<<" "<<war()<<"\n";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	REP(i,1,t+1)
		solve(i);
	return 0;
}

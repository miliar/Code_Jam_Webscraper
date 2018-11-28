#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <iomanip>
#include <utility> 

using namespace std;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))

#define all(V) V.begin(), V.end()
#define sz(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define Pi 3.14159265358979

#define pp(a) cout<<a[i].first<<" "<<a[i].second<<"\n";

typedef long long ll;
typedef unsigned long long llu;
typedef vector <ll> vi;
typedef long double ld;
typedef pair <ll, ll> pii;

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

ll count(string s,int r)
{	
	if(r==1) return (s[0]=='-')?1:0;

	if(s[0]=='+') return (r%2==0)?r:r-1;

	if(s[0]=='-')	return (r%2==1)?r:r-1;
}

void solve()
{
	ll t,ans;char prev;string s,x;

	cin>>t;

	FOR(k,1,t+1)
	{	
		cin>>s;

		prev=s[0];
		x.clear();

		FOR(i,1,s.length())
		{
			if(s[i]!=prev)x.pb(prev);
			prev=s[i];
		}

		x.pb(prev);

		ans=count(x,x.length());

		cout<< "Case #" << k <<": "<< ans <<"\n";
	}	
}

int main() 
{
	ios::sync_with_stdio(false);cin.tie(0);

	ld stime = gett();

	solve();

	cerr << "Time: "<< gett() - stime << endl;

	return 0;
}   

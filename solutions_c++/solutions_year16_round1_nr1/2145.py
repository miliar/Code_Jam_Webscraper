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

void solve()
{
	ll t;string s,ans,a;

	cin>>t;

	FOR(k,1,t+1)
	{	
		cin>>s;

		FOR(i,0,s.length())
		{
			a=s[i];

			if(ans[0]<=a[0])ans=a.append(ans);
			else ans=ans.append(a);
		}

		cout<< "Case #" << k <<": "<< ans <<"\n";

		ans.clear();
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

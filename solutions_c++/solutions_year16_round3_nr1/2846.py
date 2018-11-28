    
    
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
	ll t;int n;int a[40];

	cin>>t; vector<string> ans;

	string s="";

	FOR(k,1,t+1)
	{	
		cin>>n;

		int sum=0;

		FOR(i,0,n){cin>>a[i];sum+=a[i];}

		int mini=0;

		FOR(i,0,n)
		{
			if(a[mini]>a[i])mini=i;
		}

		int f=a[mini];
		int p=0;int q=0;

		while(p==0)
		{
			p=1;

			int maxi=0;

			FOR(i,0,n)
			{
				if(a[maxi]<a[i])maxi=i;
			}

			if(a[maxi]>f){s="";s+='A'+maxi;ans.pb(s);a[maxi]--;p=0;sum--;}
		}

		s="";

		if(sum%2==0)q=0;
		else q=1;
		
		FOR(i,0,f)
		FOR(j,0,n)
		{if(q%2==0)s="";s+='A'+j;if(q%2==1)ans.pb(s);q++;}

		if(q%2==1)ans.pb(s);

		// cout<<ans.size();
		cout<< "Case #" << k <<": ";

		FOR(i,0,ans.size()) sum-=ans[i].length();
		FOR(i,0,ans.size()) cout<<ans[i]<<" ";
		// cout<<sum;
		// cout<<ans[ans.size()-2]<<ans[ans.size()-1];

		ans.clear();

		cout<<"\n";
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

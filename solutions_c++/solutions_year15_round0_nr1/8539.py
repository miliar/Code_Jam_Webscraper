#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <string>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define REP(i,p,n) for(int i=p;i<n;++i)
#define rep(i,n) REP(i,0,n)

typedef long long int ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
typedef vector<pii> vpii;
typedef vector<vint> det1;
typedef vector<vpii> det2;

int main()
{
	int T; cin>>T;

	rep(i,T)
	{
		int t; cin>>t;
		string s; cin>>s;

		int ans = 0, sum = 0;
		rep(j,s.size())
		{
			int rest = sum < j ? j - sum : 0;
			ans += rest;
			sum += rest + (s[j]-'0');
		}

		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}

	return 0;
}

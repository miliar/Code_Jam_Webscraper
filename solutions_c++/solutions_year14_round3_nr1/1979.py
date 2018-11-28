#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <iomanip>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef istringstream iss;
typedef ostringstream oss;

map< ll,map<ll,bool> > m;
ll t,tt,a,b,r;

ll gc(ll x,ll y)
{
	ll r;
	while(y)
	{
		r=x%y;
		x=y;
		y=r;
	}
	return x;
}

ll rec(ll ans,ll x,ll y)
{
	ll g;
	while(x<y)
	{
		x<<=1;
		g=gc(x,y);
		x/=g;
		y/=g;
		if(m[x][y]==1) return 0;
		m[x][y]=1;
		ans++;
	}
	if(x==y) return ans;
	if(rec(0,x-y,y)==0) return 0;
	return ans;
}

int main(){
	#ifndef ONLINE_JUDGE
 		freopen("A-small-attempt1.in", "r", stdin);
		freopen("vd.out", "w", stdout);
	#endif
	ios_base::sync_with_stdio(false);
	int t;
	ld p, q;
	string s = "impossible";
	char c;
	cin >> t;
	for(int i = 1; i <= t; i++){
		cin  >> p >> c >> q;
		m[p][q]=1;
		ll kq  = rec(0, p, q);
		if (kq == 0) cout << "Case #" <<  i <<  ": " << s << endl;
		else cout << "Case #" <<  i <<  ": " << kq << endl;
		
		m.clear();
	}

	return 0;
}




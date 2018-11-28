#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime> 
using namespace std;

typedef long long ll;

bool ok(ll x) {
	stringstream ss; ss<<x;
	string s; ss>>s;
	int sz=s.size();
	for (int i=0; i<sz; i++)
		if(s[i]!=s[sz-1-i]) return false;
	return true;
}

ll str2num(string s) {
	stringstream ss(s); ll ans; ss>>ans; return ans;
}

ll lim=10000000;
ll len=8;

int main() {
	queue<string> q;
	q.push("");
	for (char ch='0'; ch<='9'; ch++) {
		string cur; cur+=ch;
		q.push(cur);
	}

	set<ll> st;
	vector<ll> pal;
	while(!q.empty()) {
		string cur=q.front();
		ll num = str2num(cur);
		if( num < lim )
			st.insert(num);
		q.pop();

		for (char ch='0'; ch<='9'; ch++) {
			string nxt=ch+cur+ch;
			if( nxt.size() < len )
				q.push(nxt);
		}
	}

	for(set<ll>::iterator it=st.begin(); it!=st.end(); it++)
		pal.push_back((*it));

	int sz=pal.size();

	vector<ll> v;

	for (int i=0; i<sz; i++) {
		ll cur=pal[i], ans=cur*cur;
		if( ok(ans) )
			v.push_back(ans);
	}

	sz=v.size();
	int t; cin>>t;
	for (int c=1; c<=t; c++) {
		ll A,B; cin>>A>>B;

		int ans=0;
		for (int i=0; i<sz; i++) {
			ll cur=v[i];
			if(A<=cur && cur<=B) ans++;
		}

		cout << "Case #" << c << ": " << ans << endl;
	}

	return 0;
}

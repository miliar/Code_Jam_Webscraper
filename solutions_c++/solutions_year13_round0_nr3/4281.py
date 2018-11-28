#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define ll long long
#define inf 1 << 30
#define fori(i,j,n) for (ll i = j; i <= n; i++)
#define ford(i,n,j) for (ll i = n; i >= j; i--)
#define every(t) t.begin(),t.end()
#define pb(t) push_back(t)
#define mk(a,b) make_pair(a,b)

void openFiles() {
    freopen("input.txt", "r",stdin);
    freopen("output.txt","w",stdout);
}

ll precalc[44] = { 1 , 2 , 3 , 11 , 22 , 101 , 111 , 121 , 202 , 212 , 1001 , 1111 , 2002 , 10001 , 10101 , 10201 , 11011 , 11111 , 11211 , 20002 , 20102 , 100001 , 101101 , 110011 , 111111 , 200002 , 1000001 , 1001001 , 1002001 , 1010101 , 1011101 , 1012101 , 1100011 , 1101011 , 1102011 , 1110111 , 1111111 , 2000002 , 2001002 };

int t;

bool isPal(string & s) {
	fori(i,0,s.size() / 2)
			if (s[i] != s[s.size() - 1 - i])
				return false;
	return true;
}

ll stringToInt(string & s) {
	ll n = 0;
	fori(i,0,s.size()-1)
		n = n * 10 + s[i];
	return n;
}

string intToString(ll n) {
	string s = "";
	while(n) {
		s = char('0' + n % 10) + s;
		n /= 10;
	}
	return s;
}

int main() {
	openFiles();
	cin>>t;
	int k = 0;
	ll a,b,c;
	while(k++ < t) {
		cin>>a>>b;
		int ans = 0;
		fori(i,0,40)
			if (precalc[i] != 0) {
				c = precalc[i];
				c *= c;
				if (a <= c && b >= c)
					ans++;
			}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
    return 0;
}

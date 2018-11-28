#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
typedef long long LL;
typedef pair<int,int> PT;
typedef vector<int> VI;
typedef vector<VI> VVI;
template<typename T> ostream& operator<<(ostream& s, vector<T>& v)
{ s << '{'; FOR(i,0,v.size()) s << (i ? "," : "") << v[i]; return s << '}'; }
template<typename S, typename T> ostream& operator<<(ostream &s, pair<S,T> const& p)
{ return s << '(' << p.first << ',' << p.second << ')'; }

int main() {
	int TC;
	cin >> TC;
	FOR(tc,1,TC+1) {
		string s,r;
		cin >> s;
		FOR(i,0,s.size()) {
			if (!(r.empty() || r[0] <= s[i])) r += s[i]; else r = s[i] + r;
		}
		cout << "Case #" << tc << ": " << r << endl;
	}
}

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
	int TC,N;
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> N;
		VI cnt(2501);
		FOR(n,0,2*N-1) FOR(m,0,N) {
			int x; cin >> x; cnt[x]++;
		}
		VI a;
		cout << "Case #" << tc << ":";
		FOR(i,1,2501) if (cnt[i] % 2) cout << " " << i;
		cout << endl;
	}
}

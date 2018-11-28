#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <cassert>
#include <functional>
#include <queue>
#include <cstring>

#define rep(i,n) for(int i=0; i< (n); ++i)
#define fori(i,st,en) for(int i=(st); i<(en); ++i)
#define ford(i,st,en) for(int i=(st); i>(en); --i)
#define mp(x,y) make_pair((x), (y))
#define all(v) v.begin(), v.end()
#define sfi(n) scanf("%d", &n)
#define pb(x) push_back(x)
#define Fi first
#define Se second

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector< pi > vpi;

struct quat {
	bool neg;
	int val; // [i,j,k,1]
	quat():neg(0),val(3) {}
	quat(char c):neg(false) {
		val = c-'i';
	}
	//quat(const quat& b):neg(b.neg), val(b.val) {}

	quat operator*(const quat& b) const {
		quat c;
		c.neg = neg xor b.neg;
		if(val==3) {
			c.val = b.val;
			return c;
		}
		if(b.val==3) {
			c.val = val;
			return c;
		}
		if(val==b.val) {
			c.val = 3; c.neg = !c.neg;
			return c;
		}
		if( (b.val-val+3)%3 == 1 ) {
			c.val = (b.val+1)%3;
			return c;
		}
		c.val = (val+1)%3;
		c.neg = !c.neg;
		return c;
	}
	bool operator==(const quat& b) {
		return neg==b.neg and val==b.val;
	}
	bool operator!=(const quat& b) {
		return !(*this == b);
	}
	friend ostream& operator<<(ostream& out, quat q) {
		if(q.neg) out << '-';
		if(q.val==3)
			out << "1";
		else
			out << char(q.val+'i');
	}
};

int solve() {
	int X,L,n;
	string a,s;
	cin >> L >> X >> a;
	quat QQ[3] = {'i','k','j'};
	QQ[2].neg = true;
	QQ[2].val = 3;
	rep(i,X)
		s = s+a;
	n = s.length();
	vector<quat> V;
	V.reserve(n);
	V.pb(quat(s[0]));
	for(int i=1; i<n; ++i) {
		V.pb(V[i-1]*quat(s[i]));
	}int cnt=0;
	if(V[n-1] != QQ[2])
		return false;
	for(int i=0; i<n and cnt<2; ++i) {
		if(V[i]==QQ[cnt])
			cnt++;
	}
	if(cnt==2)
		return 1;
	return 0;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T,ans;
	string msg[] = {"NO", "YES"};
	cin >> T;
	for(int tc=1; tc<=T; ++tc) {
		ans = solve();
		cout << "Case #" << tc << ": " << msg[ans] << endl;
	}
}


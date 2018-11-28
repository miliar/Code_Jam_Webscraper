#include <bits/stdc++.h>

#define ms(ar,a) memset(ar, a, sizeof(ar))
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<
#define pb push_back
#define mp make_pair
#define INF 0x3f3f3f3f
const double PI = acos(-1.0);
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(a) scanf("%s", a)
#define fr(a,b) for(int a = 0; a < b; a++)
#define frr(a,b,c) for(int a = b; a < c; a++)
#define frm(t,i,m) for(t::iterator i = m.begin(); i != m.end(); i++)
#define pri(x) printf("%d\n", x)
#define ll long long
#define vi vector<int>
#define vii vector< vi >
#define pii pair<int, int>
#define mii map<int, int>
#define wtout freopen("out.txt", "w", stdout)
#define all(vec) vec.begin(), vec.end()
#define tri(x) (x*x + x)/2
#define pm(i,b,e) i+i, b, (b+e)/2
#define sm(i,b,e) i+i+1, (b+e)/2, e
#define F first
#define S second
#define sz size()
#define ln puts("")

using namespace std;

double a[1005], b[1005];
int cn = 0, n, s, e;

int go() {
	int ret = 0;
	s = 0; e = n;
	fr(x, n) {
		if (a[x] > b[e-1]) {
			ret++; s++;
		} else if (a[x] > b[s]) {
			ret++; s++;
		} else e--;
	}
	return ret;
}

int procwar() {
	int ret = 0, p;
	set<double> cb = set<double>(b, b+n);
	set<double>::iterator it;
	fr(x, n) {
		it = cb.upper_bound(a[n-x-1]);
		if (it == cb.end()) {
			ret++;
			cb.erase(*(cb.begin()));
		} else {
			cb.erase(*it);
		}
	}
	return ret;
}

int main() {
	//freopen("D-large.in", "r", stdin);
	//wtout;
	int t;
	sc(t);
	while (t--) {
		printf("Case #%d: ", ++cn);
		sc(n);
		fr(x, n) scanf("%lf", a+x);
		fr(x, n) scanf("%lf", b+x);
		sort(a, a+n);
		sort(b, b+n);
		printf("%d %d\n", go(), procwar());
	}
	return 0;
}

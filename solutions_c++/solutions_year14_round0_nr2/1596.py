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

double c, f, x, acc, last, ans;
int farm;

int main() {
	//freopen("B-large.in", "r", stdin);
	//wtout;
	int t, cn = 1;
	sc(t);
	while (t--) {
		printf("Case #%d: ", cn++);
		scanf("%lf%lf%lf", &c, &f, &x);
		acc = 0.0; last = x/2.0;
		farm = 0;
		while (1) {
			ans = acc + c/(2.0 + farm*f) + x/(2.0 + f*(farm+1));
			//db(farm+1 _ last _ ans _ acc);
			if (ans > last) break;
			acc += c/(2.0 + farm*f);
			last = ans; farm++;
		}
		printf("%.7lf\n", last);
	}
	return 0;
}

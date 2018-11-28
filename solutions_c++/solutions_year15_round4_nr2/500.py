#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

const int oo = 0x3f3f3f3f;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

#define N 29

int main() {
	double v, x, r[N], c[N];
	int n;

	int t, cn = 1;
	sc(t); while (t--) {
		printf("Case #%d: ", cn++);
		sc(n);
		scanf("%lf%lf", &v, &x);
		
		rp(i, n) {
			scanf("%lf%lf", r+i, c+i);
		}
		
		if (n== 1) {
			if (c[0] != x) puts("IMPOSSIBLE");
			else printf("%.8lf\n", v/r[0]);
		} else {
			if (c[0] != x && c[1] == x) {
				swap(c[0], c[1]);
				swap(r[0], r[1]);
			}
			if (c[0] != x) {
				if ((c[0] < x)^(c[1] < x)) {
					double p = (x-c[1])/(c[0]-c[1]);
					double q = 1.0-p;
					double v1 = p*v, v2 = q*v;
					
					printf("%.8lf\n", max(v1/r[0], v2/r[1]));
				} else puts("IMPOSSIBLE");
			} else if (c[1] != x) {
				printf("%.8lf\n", v/r[0]);
			} else {
				printf("%.8lf\n", v/(r[0]+r[1]));
			}
		}
	}
	return 0;
}

























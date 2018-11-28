#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>


using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

void solve(int testCase) {
	printf("Case #%d: ", testCase);
	ll b;
	int n;
	scanf(LLD"%d", &b, &n);
	vll a(37, 0);
	for (int i = 0; i < n; i++)
		scanf(LLD, &a[i]);
	n = 37;
	sort(a.begin(), a.end());
	double ans = 0;
	for (int w = 1; w < n; w++) {
		ll suma = 0;
		for (int i = 0; i < w; i++)
			suma += a[i];	
		ll h = a[w - 1];
		//eprintf("%d %d\n", n, w);
		ll points = h * w - suma;
		//eprintf("%I64d %d %I64d %I64d\n", h, w, suma, points);
		ll other = count(a.begin() + w, a.begin() + n, a[w - 1]);
		int realw = other + w;
		//eprintf("w=%d points=%I64d,other=%I64d,realw=%d\n", w, points, other, realw);
		while (realw < n && points + other <= b) {
			//eprintf("w=%d points=%I64d,other=%I64d,realw=%d\n", w, points, other, realw);
			//eprintf("update ans with %.18lf\n", points * (36.0 - w) / w - other);
			ans = max(ans, points * (36.0 - w) / w - other);
			if (a[realw] - 1 == h) {
				realw += count(a.begin() + realw, a.begin() + n, h + 1);
				other += realw - w;
				points += w;
				++h;
			} else {
			  ll toadd = min(a[realw] - 1 - h, (b - points - other) / realw);
			  if (!toadd)
			  	break;
			  h += toadd;
			 	points += toadd * w, other += toadd * (realw - w);
			}
		}
	}

	printf("%.18lf\n", ans);
	//exit(0);
}

int main() {
	srand(rdtsc());
#ifdef DEBUG
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);
#endif
	
	int testCase = 0, n;
	while (scanf("%d", &n) >= 1) {
		for (int i = 0; i < n; i++)
			solve(++testCase);
		//break;
	}
	return 0;
}

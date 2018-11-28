#include <iostream>
#include <cstdio>
#include <list>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
using namespace std; 

#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define forit(it,S) for(__typeof(S.begin()) it = S.begin(); it != S.end(); ++it)
#ifdef WIN32
	#define I64d "%I64d"
#else
	#define I64d "%lld"
#endif

typedef pair <int, int> pi;

typedef pair <pi, int> pii;
const int mod = 1000002013;


int n, m, an;
pii a[111111];
list <pi> q;

int calc(int n, int k) {
	long long  res = 1LL * (n + n - k + 1) * k / 2;
	return int(res % mod);
}

int main() {
	int tests;
	scanf("%d", &tests);		
	for (int casenum = 1; casenum <= tests; ++casenum) {
		scanf("%d%d", &n, &m);
		an = 0;
		int normPay = 0;
		for (int i = 0; i < m; ++i) {
			int l, r, kol;
			scanf("%d%d%d", &l, &r, &kol);
			normPay = (1LL * calc(n, r - l) * kol + normPay) % mod;
			a[an++] = mp(mp(l, 0), kol);
			a[an++] = mp(mp(r, 1), kol);
		}
		sort(a, a + an);
		int lessPay = 0;
		for (int i = 0; i < an; ++i) {
			
			int x = a[i].f.f, tip = a[i].f.s, kol = a[i].s;
			//printf("%d %d %d\n", x, tip, kol);
			//cout.flush();
			if (tip == 0)
				q.push_front(mp(x, kol));
			else {
				while (kol > 0) {
					pi fr = q.front();
					q.pop_front();
					int kk = min(kol, fr.s);
					fr.s -= kk;
					kol -= kk;
					int cur = calc(n, x - fr.f);
					lessPay = (1LL * cur * kk + lessPay) % mod;				
					if (fr.s)
						q.push_front(fr);
				}
			}	
		}
		int res = normPay - lessPay;
		if (res < 0) res += mod;
		printf("Case #%d: %d\n", casenum, res);
	}
	return 0;		
}

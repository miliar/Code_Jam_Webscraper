#include <cstdlib>
#include <cstdio>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;
int t, n;
double a[1111], b[1111], ar[1111], br[1111];
int p[1111];
pair<double, int> ab[2222];

void solve(int t) {
	scanf("%d", &n);
	set<double> B;
	for (int i = 0 ; i < n ; i++ )scanf("%lf", &a[i]);
	for (int i = 0 ; i < n ; i++ ) {
		scanf("%lf", &b[i]);

	}
	sort(a, a + n);
	sort(b, b + n);
	/*
	for (int i = 0 ; i < n ; i ++) printf("%lf ", a[i]);
	puts("");
	for (int i = 0 ; i < n ; i ++) printf("%lf ", b[i]);
	puts("");      */
	
	


	int z = 0, y = 0;
	// z
	for (int i = 0 ; i < n ; i ++) ab[i] = make_pair(a[i], 1);
	for (int i = n ; i < 2*n ; i ++) ab[i] = make_pair(b[i - n], 2);
	sort(ab, ab + 2*n);
	int best = 0, c1 = 0, c2 = 0;
	for (int i = 2*n - 1 ; i >= 0 ; i --) {
		if (ab[i].second == 1) c1 ++;
		else c2 ++;
		best = max(c1 - c2, best);
	}
	               /*
	for (int i = 0 ; i < n ; i ++) p[i] = i;
	do {
		int loc = 0;
		B.clear();
		for (int i = 0 ; i < n ; i ++) 		
			B.insert(b[i]);
		for (int i = 0 ; i < n ; i ++) {
			set<double>::iterator it = B.lower_bound(a[p[i]]);
			if (it == B.end()) {
				B.erase(B.begin());
				loc ++;
			}
			else 
				B.erase(it);
		}
		z = max(z, loc);
	} while(next_permutation(p, p + n));

	assert(z == best);
	*/
	for (int r = 0 ; r < n ; r ++) {
		for (int i = r ; i < n ; i ++)
			ar[i - r] = a[i];
		for (int i = 0 ; i < n - r; i ++)
			br[i] = b[i];
		bool ok = 1;
		for (int i = 0 ; i < n - r ; i ++) {
			if (ar[i] < br[i]) ok = 0;
		}
		if (ok) y = max(y, n - r);
	}
	z = best;


	printf("Case #%d: %d %d\n", t, y, z);



}


int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	scanf("%d", &t);
	for (int i = 1 ; i <= t ; i++) solve(i);
	return 0;
}
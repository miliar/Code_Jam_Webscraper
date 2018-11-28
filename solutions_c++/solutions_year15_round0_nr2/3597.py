#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>                                                                       
#include <ctime>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define forn(i, n) for (int i = 0; i < (int)n; i++)
#define fore(i, b, e) for (int i = (int)b; i <= (int)e; i++)
#define f first
#define s second
#define next qwertyusdfgh
#define read(x) scanf("%d", &x)
#define write(x) printf("%d ", x)
#define writeln(x) printf("%d\n", x)
#define pb push_back
#define mp make_pair

const int maxN = 1e4;

int a[maxN];

int main() {

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> a[i];
		int ans = 1001;
		for (int j = 1; j <= 1000; j++) {
			int cur = j;
			for (int i = 0; i < n; i++)
				if (a[i] > j) {
					cur += a[i] / j;
					if (a[i] % j == 0)
						cur--;
				}
			ans = min(ans, cur);
		}
	    printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}
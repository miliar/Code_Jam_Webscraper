
#include <bits/stdc++.h>

using namespace std;

typedef long long      ll;
typedef pair<int, int> ii;
typedef vector<int>    vi;
typedef vector<ll>    vll;
typedef vector<ii>    vii;
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define INF 2000000000
#define MAX_N 1010

int arr[MAX_N];

int main() {
	freopen ("in.txt", "r", stdin);
	freopen ("out.txt","w", stdout);
	int n;
	scanf(" %d", &n);
	for (int CA = 1 ; CA <= n; CA++) {
		int x, r, c;
		scanf(" %d %d %d", &x, &r, &c);
		if (x==1) {
			printf("Case #%d: GABRIEL\n", CA);
		} else if (x == 2) {
			if (r % 2 == 0 || c % 2 == 0) {
				printf("Case #%d: GABRIEL\n", CA);
			} else {
				printf("Case #%d: RICHARD\n", CA);
			}
		} else if (x == 3) {
			if (r == 3 && c == 1 || r == 1 && c == 3) printf("Case #%d: RICHARD\n", CA);
			else {
				if (r % 3 == 0 || c % 3 == 0) {
					printf("Case #%d: GABRIEL\n", CA);
				} else {
					printf("Case #%d: RICHARD\n", CA);
				}
			}
		} else {
			int mn = min(r, c), mx = max(r, c);
			if (mn == 3 && mx == 4) printf("Case #%d: GABRIEL\n", CA);
			else if (mn == 4 && mx == 4) printf("Case #%d: GABRIEL\n", CA);
			else printf("Case #%d: RICHARD\n", CA);
		}
	}
}


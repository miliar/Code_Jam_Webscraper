#include <bits/stdc++.h>
using namespace std;

typedef long long     ll;
typedef double        dbl;
typedef long double   ld;

#define X             first
#define Y             second
#define mp            make_pair
#define pb            push_back
#define sz(x)         (int)(x).size()
#define all(x)        x.begin(),x.end()

#ifdef ROMCHELA
#    define D(x)      cout<<#x<<" = "<<(x)<<endl
#    define Ds()      cout<<"------------"<<endl
#else
#    define D(c)      ((void)0)
#    define Ds(x)     ((void)0)
#endif

const int maxn = 2000 * 100 + 10;


int main() {
#ifdef ROMCHELA
	assert(freopen("input.txt", "r", stdin));
	assert(freopen("output.txt", "w", stdout));
#endif

	int t;
	scanf("%d", &t);
	for (int q = 0; q < t; q++) {
		int n;
		scanf("%d ", &n);
		string s;
		getline(cin, s);
		int answer = 0;
		int cur = 0;
		for (int j = 0; j < sz(s); j++) {
			if (s[j] != '0') {
				if (cur >= j) {
					cur += s[j] - '0';
				} else {
					answer += (j - cur);
					cur = j + s[j] - '0';;
				}
			}
		}
		printf("Case #%d: %d\n", q + 1, answer);
	}

#ifdef ROMCHELA
	cerr << "\nTIME ELAPSED: " << (dbl)clock() / CLOCKS_PER_SEC << " sec\n";
#endif
	return 0;
}


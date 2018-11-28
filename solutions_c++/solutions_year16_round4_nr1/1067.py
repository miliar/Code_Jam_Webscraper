#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

void solve(int a, int b, int c) {
	if(a+b+c == 1) {
		if(a == 1)	putchar('P');
		if(b == 1)	putchar('R');
		if(c == 1)	putchar('S');
		return ;
	}

	int x = a/2, y = b/2, z = c/2;
	if(a % 2 == 0) {
		solve(x, b-y, z);
		solve(x, y, c-z);
	}
	if(b % 2 == 0) {
		solve(a-x, y, z);
		solve(x, y, c-z);
	}
	if(c % 2 == 0) {
		solve(a-x, y, z);
		solve(x, b-y, z);
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		int n, a, b, c;
		scanf("%d%d%d%d", &n, &b, &a, &c);

		printf("Case #%d: ", kase);
		debug("%d %d %d : ", a, b, c);
		int x = max(a, max(b, c)), y = min(a, min(b, c));
		if(x-y != 1) {
			puts("IMPOSSIBLE");
			continue;
		}

		solve(a, b, c);
		putchar('\n');
	}
    
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

typedef long long int lli;

#define MOD 1000000007

#define scan(x) scanf("%d", &x)
#define print(x) printf("%d\n", x)

#define scan_lli(x) scanf("%lld", &x)
#define print_lli(x) printf("%lld\n", x)

#define scanc(x) scanf("%c", &x)
#define printc(x) printf("%c", x)

#define scans(x) scanf("%s", x)
#define prints(x) scanf("%s\n", x)

#define for_up(v, s, e) for (int v=s; v<e; v++)
#define for_down(v, s, e) for (int v=s; v>=e; v--)

#define vi vector<int>
#define pii pair<int, int>
#define vpii vector< pair<int, int> >

#define pb push_back
#define mp make_pair

#define fs first
#define sc second

lli solve (lli n) {
	
	bool v[10];
	memset(v, false, sizeof v);
	
	lli m = n;
	int cnt = 0;
	while (cnt < 10) {
		lli x = m;
		while (x > 0) {
			int d = x % 10;
			if (!v[d]) {
				cnt++;
				v[d] = true;
			}
			x /= 10;
		}
		m += n;
	}
	
	return m-n;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int t;
	scan(t);
	
	for_up (te, 1, t+1) {
		lli n;
		scan_lli(n);
		
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", te);
		}
		
		else {
			printf("Case #%d: %lld\n", te, solve(n));
		}
	}

	return 0;
}


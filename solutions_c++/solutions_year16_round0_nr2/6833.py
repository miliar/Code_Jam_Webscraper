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

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int t;
	scan(t);
	
	for_up (te, 1, t+1) {
		string s;
		cin >> s;
		
		int l = s.length();
		int ans = 0;
		
		for_up (i, 1, l) {
			if (s[i] != s[i-1]) {
				ans++;
			}
		}
		
		if (s[l-1] != '+') {
			ans++;
		}
		
		printf("Case #%d: %d\n", te, ans);
	}

	return 0;
}


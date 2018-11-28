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
#define prints(x) fscanf(out, "%s\n", x)

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
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
	
    int T;
    scan(T);

    for_up (t, 1, T+1) {
		string s;
		cin >> s;
		
		int l = s.length();
		
		string ans(1, s[0]);
		
		for (int i=1; i<l; i++) {
			if (s[i] >= ans[0]) {
				ans = string(1, s[i]) + ans;
			}
			else {
				ans += string(1, s[i]);
			}
		}
		
		printf("Case #%d: ", t);
		cout << ans << '\n';
	}
	
	fclose(stdin);
	fclose(stdout);

	return 0;
}


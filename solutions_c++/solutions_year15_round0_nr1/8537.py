#include <bits/stdc++.h>

typedef unsigned long long llu;
typedef long long ll;

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define reset(a, b) memset(a, b, sizeof(a))
#define dump(a) cerr << #a << " = " << a << endl

using namespace std;

void open(string s) {
    #ifndef ONLINE_JUDGE
    freopen(s.c_str(), "r", stdin);
    #endif // ONLINE_JUDGE
}

int main() {
	int t, c = 1;
	scanf("%d", &t);
	
	while (t--) {
		int ans = 0, n;
		scanf("%d", &n);
		
		char ov[n+2];
		scanf("%s", ov);
		
		int prog = ov[0] - (int) '0';
		for (int i = 1; i <= n; i++) {
			if (prog >= i)
				prog += ov[i] - (int) '0';
			else {
				ans += i - prog;
				prog = i + ov[i] - (int) '0';
			}
		}
		
		printf("Case #%d: %d\n", c++, ans);
	}
}
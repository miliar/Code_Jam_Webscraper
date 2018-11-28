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

int main() {

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		string s;
		cin >> n >> s;
		int ans = 0;
		int cur = 0;
		for (int i = 0; i <= n; i++) {
			if (cur < i) {
				ans += i - cur;
				cur = i;
			}
			cur += s[i] - '0';
		}
		printf("Case #%d: %d\n", t, ans);
	}	
	
	return 0;
}
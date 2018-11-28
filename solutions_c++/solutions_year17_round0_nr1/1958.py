#include <bits/stdc++.h>

#define ll long long
#define __(x) cout << #x << " : " << x << endl;
#define out(a, i, n) for (int i = 0; i < n; i++) cout << a[i] << " "; cout << endl;
#define mp make_pair
#define pb push_back
#define forn(i, n) for (int i = 0; i < n; i++)
#define N 1111

#define INOUT
#define TIME	

using namespace std;

void print(int test, int ans) {
	cout << "Case #" << test << ": " << ans << endl;
	//printf("Case #%d: %d\n", test, ans);
}

void print(int test, string ans) {
	cout << "Case #" << test << ": " << ans << endl;
}

int flips[N];

int main()
{
#ifdef INOUT
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	
	int tests;
	cin >> tests;
	ll ans = 0;
	for (int test = 1; test <= tests; test++)
	{
		for (int i = 0; i < N; i++) {
			flips[i] = 0;
		}
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		s = '+' + s;
		for (int i = 1; i < s.length() - k + 1; i++) {
			flips[i] = flips[i - 1];
			int here = s[i] == '-';
			here += flips[i] - flips[max(i - k, 0)];
			if (here & 1) {
				flips[i]++;
				ans++;
			}
		}
		bool has_ans = true;
		for (int i = s.length() - k + 1; i < s.length(); i++) {
			flips[i] = flips[i - 1];
			int here = s[i] == '-';
			here += flips[i] - flips[max(i - k, 0)];
			if (here & 1) {
				has_ans = false;
			}
		}
		if (has_ans) {
			print(test, ans);
		} else {
			print(test, "IMPOSSIBLE");
		}
	}

#ifdef TIME
	cerr << (double) clock() / CLOCKS_PER_SEC;
#endif 
	return 0;
}

#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
using namespace std;
#define rep(i, N) for (decltype(N) i = 0; i < N; ++i)
#define dep(i, N) for (decltype(N) i = N - 1; i >= 0; --i)
#define FOR(i, A, B) for (decltype(B) i = A; i <= B; ++i)
#define FORD(i, B, A) for (decltype(B) i = B; i >= A; --i)
#define len(A) (int)A.size()
#define all(A) A.begin(), A.end()
#define move _move

typedef long long int64;
typedef long double ld;

bool u[10];

int main()
{
	ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	rep(t, T)
	{
		string s;
		cin >> s;
		cout << "Case #" << t + 1 << ": ";
		string s1 = "";
		s1 += s[0];
		FOR(i, 1, len(s) - 1)
			if (s[i] != s[i - 1])
				s1 += s[i];
		cout << (s1[0] == '+' ? len(s1) - len(s1) % 2 : len(s1) + len(s1) % 2 - 1) << endl;
	}
	return 0;
}

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
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	rep(t, T)
	{
		int64 N;
		cin >> N;
		cout << "Case #" << t + 1 << ": ";
		if (N == 0)
			cout << "INSOMNIA" << endl;
		else
		{
			memset(u, 0, sizeof(u));
			int cnt = 0;
			for (int i = 1; ; i++)
			{
				int64 x = i * N;
				while (x)
				{
					if (!u[x % 10])
						u[x % 10] = 1, cnt++;
					x /= 10;
				}
				if (cnt == 10)
				{
					cout << i * N << endl;
					break;
				}
			}
		}
	}
	return 0;
}

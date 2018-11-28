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
minstd_rand gen;
int64 mul(int64 a, int64 b, const int64 mod)
{
	return (b == 0ll ? 0ll : (b & 1) ? (mul(a, b - 1, mod) + a) % mod : (mul(a, b >> 1, mod) << 1) % mod);
}
int64 gcd(int64 a, int64 b)
{
	while (b > 0)
	{
		int64 t = a % b;
		a = b;
		b = t;
	}
	return a;
}
int64 bpow(int64 a, int64 n, int64 mod)
{
	int64 res = 1ll;
	a %= mod;
	while (n > 0)
	{
		if (n & 1)
			res = mul(res, a, mod);
		a = mul(a, a, mod);
		n >>= 1;
	}
	return res;
}
bool ferma(int64 n)
{
	if (n == 2)
		return true;
	uniform_int_distribution<int64> rnd(2, n - 1);
	rep(i, 10)
	{
		int64 a = rnd(gen);
		if (gcd(n, a) != 1 || bpow(a, n - 1, n) != 1)
			return false;
	}
	return true;
}
int64 tonum(const string &s, int64 p)
{
	int64 res = 0;
	for (auto &c : s)
		res = res * p + (c - '0');
	return res;
}

int main()
{
	ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	srand(2);
	int T;
	cin >> T;
	set<string> q;
	rep(t, T)
	{
		int N, J;
		cin >> N >> J;
		cout << "Case #" << t + 1 << ":" << endl;
		rep(j, J)
		{
			string s;
			vector<int> divs;
			while (true)
			{
				divs = {};
				s = "1";
				rep(i, N - 2)
					s += char('0' + (rand() & 1));
				s += '1';
				if (q.count(s))
					goto endw;
				FOR(p, 2, 10)
				{
					int64 x = tonum(s, p);
					if (ferma(x))
						goto endw;
					bool flag = false;
					FOR(d, 2, 5000)
					{
						if (x % d == 0)
						{
							flag = true;
							divs.push_back(d);
							break;
						}
					}
					if (!flag)
						goto endw;
				}
				break;
			endw:;
			}
			q.insert(s);
			cout << s;
			for (int d : divs)
				cout << ' ' << d;
			cout << endl;
		}
	}
	return 0;
}

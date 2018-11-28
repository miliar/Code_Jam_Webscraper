#include<cstdio>
#include<algorithm>
#include<map>
#include<string>
using namespace std;

struct rps
{
	int r, p, s;
	rps(int r, int p, int s) : r(r), p(p), s(s) {}
	rps operator + (const rps o) const
	{
		return rps(r + o.r, p + o.p, s + o.s);
	}
	bool operator < (const rps o) const
	{
		if (r != o.r) return r < o.r;
		if (p != o.p) return p < o.p;
		return s < o.s;
	}
};

map<rps, string> m[13][3];

int foo(int a, int b)
{
	if (a == 0) return b == 1 ? 1 : 0;
	if (a == 1) return b == 2 ? 2 : 1;
	if (a == 2) return b == 0 ? 0 : 2;
}

void init()
{
	m[1][0].emplace(rps(1, 0, 1), "RS");
	m[1][1].emplace(rps(1, 1, 0), "PR");
	m[1][2].emplace(rps(0, 1, 1), "PS");
	for (int n = 2; n <= 12; n++)
	{
		for (auto r : m[n - 1][0])
		{
			for (auto s : m[n - 1][2])
			{
				m[n][0].emplace(r.first + s.first, (r.second > s.second) ? s.second + r.second : r.second + s.second);
			}
		}
		for (auto p : m[n - 1][1])
		{
			for (auto r : m[n - 1][0])
			{
				m[n][1].emplace(p.first + r.first, (r.second > p.second) ? p.second + r.second : r.second + p.second);
			}
		}
		for (auto s : m[n - 1][2])
		{
			for (auto p : m[n - 1][1])
			{
				m[n][2].emplace(p.first + s.first, (s.second > p.second) ? p.second + s.second : s.second + p.second);
			}
		}
	}
}

string solve(int n, int r, int p, int s)
{
	int nn = 1 << n;
	rps f(r, p, s);
	if (r > nn / 2 || p > nn / 2 || s > nn / 2) return "";
	for (int i = 0; i < 3; i++)
	{
		auto it = m[n][i].find(f);
		if (it != m[n][i].end()) return it->second;
	}
	return "";
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, n, r, p, s;
	scanf("%d", &T);
	init();
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d%d%d", &n, &r, &p, &s);
		string ans = solve(n, r, p, s);
		printf("Case #%d: %s\n", t,  ans.empty() ?"IMPOSSIBLE" : ans.c_str());
	}
}
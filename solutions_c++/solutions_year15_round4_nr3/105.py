#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
const LL inf = ~0ULL >> 5;

namespace Dinic {
	const int N = 46384, M = int(5e6);
	struct edge { int t; LL c; edge *op, *n; }
		ebf[M], *ec = ebf, *e[N], *er[N];
	int n, s, t, d[N];
	inline void add_edge (int s, int t, LL c)
	{
		assert(ec - ebf < M);
		*ec = (edge){t, c, ec + 1, er[s]}; er[s] = ec++;
		*ec = (edge){s, 0, ec - 1, er[t]}; er[t] = ec++;
	}
	inline void reset ()
	{
		memset(er, 0, sizeof(er[0]) * (n + 1));
		memset(d, 0, sizeof(d[0]) * (n + 1));
		n = 0; ec = ebf;
	}
	bool modlabel ()
	{
		static int que[M];
		int l(0), r(0), x, y;
		memcpy(e, er, sizeof(er[0]) * (n + 1));
		memset(d, 0xff, sizeof(d[0]) * (n + 1));
		d[que[++r] = s] = 0;
		while (l != r)
			for (edge *i = er[x = que[++l]]; i; i = i->n)
				if (i->c && d[y = i->t] < 0) d[que[++r] = y] = d[x] + 1;
		return d[t] >= 0;
	}
	LL augument (int x, LL c)
	{
		if (x == t) return c;
		LL r(c), de; int y; edge *i;
		for (i = e[x]; i; i = i->n)
			if (i->c && d[x] + 1 == d[y = i->t])
			{
				de = augument(y, min(r, i->c));
				i->c -= de, i->op->c += de, r -= de;
				if (!r) break;
			}
		e[x] = i;
		if (r) d[x] = -1; // CRUCIAL OPTIMIZATION
		return c - r;
	}
	LL solve (int _n, int _s, int _t)
	{
		assert(_n < N);
		LL res = 0, de; n = _n; s = _s; t = _t;
		while (modlabel()) while (de = augument(s, ~0ULL >> 4)) res += de;
		return res;
	}
}

void solve ()
{
	int n, s, t;
	cin >> n;
	string dump;
	std::getline(cin, dump);
	map<string, int> idmap{};
	s = n + 1;
	t = n + 2;
	int cnt = t;
	Dinic::reset();
	for (int i = 1; i <= n; ++i)
	{
		string line;
		std::getline(cin, line);
//		cerr << "L" << i << line << endl;
		std::istringstream inp(line);
		while (!inp.eof())
		{
			string word;
			inp >> word;
//			cout << "W" << word << endl;
			int id;
			if (idmap.count(word)) id = idmap[word];
			else
			{
				id = cnt + 1;
				Dinic::add_edge(id, id + 1, 1);
				idmap[word] = id;
				cnt += 2;
			}
			if (i == 1) // English
			{
				Dinic::add_edge(s, id, inf);
			}
			else if (i == 2)
			{
				Dinic::add_edge(id + 1, t, inf);
			}
			else
			{
				Dinic::add_edge(i, id, inf);
				Dinic::add_edge(id + 1, i, inf);
			}
		}
	}
	int rel = Dinic::solve(cnt, s, t);
	cout << rel << endl;
}

int main ()
{
	int tk;
	cin >> tk;
	for (int i = 1; i <= tk; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}


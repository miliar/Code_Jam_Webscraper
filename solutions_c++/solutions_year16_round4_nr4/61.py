#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using namespace std;

unsigned SolveD2(vector<pair<unsigned, unsigned>>& vp, unsigned x, unsigned y)
{
	if (vp.size() == 0)
	{
		assert(x == y);
		return x;
	}
	if (vp.size() == 1)
	{
		if (vp[0].first > vp[0].second)
		{
			return vp[0].first * vp[0].first + x;
		}
		else
		{
			return vp[0].second * vp[0].second + y;
		}
	}
	unsigned N = vp.size() - 1;
	unsigned best = numeric_limits<unsigned>::max();
	for (unsigned i = 0; i < (1u << N); ++i)
	{
		unsigned dx = vp[0].first, dy = vp[0].second;
		vector<pair<unsigned, unsigned>> vpn;
		for (unsigned j = 0; j < N; ++j)
		{
			if (i & (1u << j))
			{
				dx += vp[j + 1].first;
				dy += vp[j + 1].second;
			}
			else
			{
				vpn.push_back(vp[j + 1]);
			}
		}
		if (dx >= dy)
		{
			if (dx <= dy + y)
			{
				unsigned current = dx * dx + SolveD2(vpn, x, y + dy - dx);
				best = min(best, current);
			}
		}
		else
		{
			if (dy <= dx + x)
			{
				unsigned current = dy * dy + SolveD2(vpn, x + dx - dy, y);
				best = min(best, current);
			}
		}
	}
	return best;
}

unsigned SolveD1(vector<pair<unsigned, unsigned>>& vp)
{
	unsigned x = 0, y = 0;
	for (; vp.size() > 0; )
	{
		auto p = vp.back();
		if (p.first + p.second > 1)
			break;
		x += p.first;
		y += p.second;
		vp.pop_back();
	}
	return SolveD2(vp, x, y);
}

template<typename TSize>
class CTDisjointSet
{
protected:
	TSize n;
	vector<TSize> p;
	vector<unsigned> rank;
	vector<TSize> vsize;
	stack<TSize> ts;

public:
	CTDisjointSet(TSize _n)
	{
		Init(_n);
	}

	void Init(TSize _n)
	{
		n = _n;
		p.resize(n);
		for (TSize i = 0; i < n; ++i)
			p[i] = i;
		rank.resize(n);
		fill(rank.begin(), rank.end(), 0);
		vsize.resize(n);
		fill(vsize.begin(), vsize.end(), 1);
	}

	void Union(TSize i1, TSize i2)
	{
		UnionI(Find(i1), Find(i2));
	}

	TSize Find(TSize x)
	{
		TSize px = p[x];
		if (px == x)
			return px;
		TSize ppx = p[px];
		if (ppx == px)
			return px;
		do
		{
			ts.push(x);
			x = px;
			px = ppx;
			ppx = p[px];
		} while (px != ppx);
		while (!ts.empty())
		{
			x = ts.top();
			p[x] = ppx;
			ts.pop();
		}
		return ppx;
	}

	TSize GetSize(TSize x)
	{
		return vsize[Find(x)];
	}

	vector<TSize> GetRepresentatives() const
	{
		vector<TSize> vr;
		for (TSize i = 0; i < n; ++i)
		{
			if (p[i] == i)
				vr.push_back(i);
		}
		return vr;
	}

protected:
	void UnionI(TSize i1, TSize i2)
	{
		if (i1 == i2) return;
		if (rank[i1] > rank[i2])
		{
			p[i2] = i1;
			vsize[i1] += vsize[i2];
		}
		else
		{
			p[i1] = i2;
			if (rank[i1] == rank[i2])
				++rank[i1];
			vsize[i2] += vsize[i1];
		}
	}
};

typedef CTDisjointSet<size_t> CDisjointSet;

int main()
{
	unsigned T;
	cin >> T;
	for (unsigned it = 0; it < T; ++it)
	{
		cout << "Case #" << it + 1 << ": ";
		unsigned N;
		cin >> N;
		CDisjointSet ds(2 * N);
		string s;
		unsigned s1 = 0;
		for (unsigned i = 0; i < N; ++i)
		{
			cin >> s;
			for (unsigned j = 0; j < N; ++j)
			{
				if (s[j] == '1')
				{
					ds.Union(i + N, j);
					++s1;
				}
			}
		}
		vector<unsigned> vd1(2*N, 0), vd2(2 * N, 0);
		for (unsigned i = 0; i < N; ++i)
		{
			vd1[ds.Find(i + N)]++;
			vd2[ds.Find(i)]++;
		}

		unsigned ss = 0;
		vector <pair<unsigned, pair<unsigned, unsigned>>> vpp;
		for (unsigned i = 0; i < 2 * N; ++i)
		{
			if (vd1[i] != vd2[i])
			{
				vpp.push_back(make_pair(vd1[i] + vd2[i], make_pair(vd1[i], vd2[i])));
			}
			else
			{
				ss += vd1[i] * vd2[i];
			}
		}
		sort(vpp.begin(), vpp.end());
		reverse(vpp.begin(), vpp.end());
		vector<pair<unsigned, unsigned>> vp;
		for (auto p : vpp) vp.push_back(p.second);
		unsigned s2 = SolveD1(vp);

		cout << s2 + ss - s1 << endl;
	}
	return 0;
}

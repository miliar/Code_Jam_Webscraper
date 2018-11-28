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

static double sqr(unsigned x)
{
	return double(x * x);
}

int main()
{
	unsigned T;
	cin >> T;
	for (unsigned it = 0; it < T; ++it)
	{
		unsigned N, S;
		cin >> N >> S;
		vector<double> vx(N), vy(N), vz(N), vdx(N), vdy(N), vdz(N);
		for (unsigned i = 0; i < N; ++i)
		{
			cin >> vx[i] >> vy[i] >> vz[i] >> vdx[i] >> vdy[i] >> vdz[i];
		}
		vector<tuple<double, unsigned, unsigned>> vt;
		for (unsigned i = 0; i < N; ++i)
		{
			for (unsigned j = i + 1; j < N; ++j)
			{
				double d = sqrt(sqr(vx[i] - vx[j]) + sqr(vy[i] - vy[j]) + sqr(vz[i] - vz[j]));
				vt.push_back(make_tuple(d, i, j));
			}
		}
		sort(vt.begin(), vt.end());
		CDisjointSet ds(N);
		double answer = 0.0;
		for (auto t : vt)
		{
			ds.Union(get<1>(t), get<2>(t));
			if (ds.Find(0) == ds.Find(1))
			{
				answer = get<0>(t);
				break;
			}
		}
		cout << "Case #" << it + 1 << ": ";
		cout << answer;
		cout << endl;
	}
	return 0;
}

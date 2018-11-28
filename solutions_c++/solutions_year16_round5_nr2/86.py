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

#include <iostream>
#include <vector>

using namespace std;

template <bool directed_edges = false>
class CTBaseGraph
{
public:
	using TSelf = CTBaseGraph<directed_edges>;

public:
	unsigned nvertices;
	vector<vector<unsigned>> edges;
	vector<vector<unsigned>> inverted_edges;

public:
	CTBaseGraph(unsigned _nvertices) : nvertices(_nvertices)
	{
		edges.resize(nvertices);
		if (directed_edges)
		{
			inverted_edges.resize(nvertices);
		}
	}

	void AddEdge(unsigned from, unsigned to)
	{
		edges[from].push_back(to);
		if (directed_edges)
		{
			inverted_edges[to].push_back(from);
		}
		else
		{
			edges[to].push_back(from);
		}
	}

	void ReadEdges(unsigned edges_to_read, bool zero_based_indexes = false)
	{
		unsigned shift = zero_based_indexes ? 0 : 1;
		for (; edges_to_read; --edges_to_read)
		{
			unsigned from, to;
			cin >> from >> to;
			AddEdge(from - shift, to - shift);
		}
	}
};

template <bool directed_edges = false>
class CTBaseTree : public CTBaseGraph<directed_edges>
{
public:
	using TBase = CTBaseGraph<directed_edges>;
	using TSelf = CTBaseTree<directed_edges>;

public:
	unsigned root;

public:
	CTBaseTree(unsigned _nvertices, unsigned _root = 0) : TBase(_nvertices), root(_root) {}

	void ReadTreeEdges()
	{
		for (unsigned i = 1; i < CTBaseGraph<directed_edges>::nvertices; ++i)
		{
			unsigned from;
			cin >> from;
			CTBaseGraph<directed_edges>::AddEdge(from, i);
		}
	}
};

using CBaseTree = CTBaseTree<false>;
using CBaseDirectedTree = CTBaseTree<true>;

using CBaseGraph = CTBaseGraph<false>;
using CBaseDirectedGraph = CTBaseGraph<true>;

static vector<double> vf;

void PreCalc(const CBaseDirectedTree& g, vector<unsigned>& vs, vector<double>& vp, unsigned node)
{
	vs[node] = 1;
	vp[node] = 1.0;
	for (unsigned c : g.edges[node])
	{
		PreCalc(g, vs, vp, c);
		vs[node] += vs[c];
		vp[node] *= vp[c];
	}
	vp[node] /= vs[node];
}

mt19937_64 rng;

string Sample(CBaseDirectedTree& g, const vector<unsigned>& vs, const vector<double>& vp, const string& s)
{
	unsigned l = g.nvertices; 
	static vector<unsigned> vc;
	vc.reserve(l);
	vc.resize(1); 
	vc[0] = 0;

	string output;
	for (; vc.size() > 0; --l)
	{
		if (vc.size() == 1)
		{
			unsigned x = vc[0];
			output += s[x];
			vc.pop_back();
			for (unsigned c : g.edges[x])
			{
				vc.push_back(c);
			}
		}
		else
		{
			uniform_int_distribution<int> uid(1, l);
			unsigned k = uid(rng), i = 0;
			for (; k > vs[vc[i]]; ++i) k -= vs[vc[i]];
			if (i != vc.size() - 1)
			{
				swap(vc[i], vc[vc.size() - 1]);
			}
			unsigned x = vc.back();
			output += s[x];
			vc.pop_back();
			for (unsigned c : g.edges[x])
			{
				vc.push_back(c);
			}
		}
	}
	return output;
}

int main()
{
	vf.push_back(1.0);
	while (vf.size() <= 100)
	{
		vf.push_back(vf.back() * vf.size());
	}

	unsigned T;
	cin >> T;
	for (unsigned it = 0; it < T; ++it)
	{
		cout << "Case #" << it + 1 << ":";
		
		unsigned N, M;
		cin >> N;
		CBaseDirectedTree g(N + 1);
		g.ReadTreeEdges();
		string s;
		cin >> s; 
		s = string(" ") + s;
		cin >> M;
		vector<string> vo(M);
		for (unsigned i = 0; i < vo.size(); ++i)
		{
			cin >> vo[i];
		}

		vector<unsigned> vs(N + 1);
		vector<double> vp(N + 1);
		PreCalc(g, vs, vp, 0);

		unsigned T = 10000;
		vector<unsigned> voc(M, 0);
		for (unsigned i = 0; i < T; ++i)
		{
			string sc = Sample(g, vs, vp, s);
			for (unsigned j = 0; j < M; ++j)
			{
				if (sc.find(vo[j]) != sc.npos)
				{
					++voc[j];
				}
			}
		}

		for (unsigned j = 0; j < M; ++j)
		{
			double d = voc[j] * 1.0 / T;
			cout << " " << d;
		}

		cout << endl;
	}
	return 0;
}

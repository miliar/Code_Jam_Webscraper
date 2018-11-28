#include <stdio.h>
#include <vector>
#include <algorithm>

struct UnionFind {
  std::vector<int> data;
  UnionFind(int size) : data(size, -1) { }
  bool unionSet(int x, int y) {
    x = root(x); y = root(y);
    if (x != y) {
      if (data[y] < data[x]) std::swap(x, y);
      data[x] += data[y]; data[y] = x;
    }
    return x != y;
  }
  bool findSet(int x, int y) {
    return root(x) == root(y);
  }
  int root(int x) {
    return data[x] < 0 ? x : data[x] = root(data[x]);
  }
  int size(int x) {
    return -data[root(x)];
  }
};

struct Edge {
	int s, e;
	double d;

	Edge()
	{}

	Edge(int a, int b, double c) : s(a), e(b), d(c)
	{}

	bool operator<(const Edge& o) const
	{
		return d < o.d;
	}
};

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N, S;
		scanf("%d%d", &N, &S);
		std::vector<double> x, y, z;
		for (int i=0; i<N; i++) {
			int a0, a1, a2, a3;
			scanf("%d%d%d%d%d%d", &a0, &a1, &a2, &a3, &a3, &a3);
			x.push_back(a0);
			y.push_back(a1);
			z.push_back(a2);
		}
		double mx = 0.0;
		//std::vector<std::vector<double> > tab(N);
		std::vector<Edge> tab;
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				tab.push_back(Edge(i, j, sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) + (z[i]-z[j])*(z[i]-z[j]))));
			}
		}
		std::sort(tab.begin(), tab.end());
		double ret = 0.0;
		UnionFind uf(N);
		for (int i=0; i<tab.size(); i++) {
			uf.unionSet(tab[i].s, tab[i].e);
			if (uf.findSet(0, 1)) {
				ret = tab[i].d;
				break;
			}
		}
		printf("Case #%d: %f\n", t, ret);
	}

	return 0;
}
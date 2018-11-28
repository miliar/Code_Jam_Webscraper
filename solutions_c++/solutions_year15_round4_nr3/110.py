#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <vector>
#include <set>
#include <sstream>

using namespace std;

const int MAXN = 20000;
const int MAXM = 320000;


struct sEdge
{
	int a, b, c, f;
};

int ss, tt, N, M;
sEdge e[MAXM];
int ea[MAXM], eb[MAXM];
int ean[MAXN], ebn[MAXN];
int nh[MAXN], h[MAXN];

// node number 1~N

void AddEdge(int a, int b, int c)
{
	e[M].a = a;  e[M].b = b;  e[M].c = c;  M++;
	e[M].a = b;  e[M].b = a;  e[M].c = c;  M++;
}

int Argu(int u, int lf)
{
	if (u == tt)  return lf;
	int nf = lf, mh = N, z = 0, x, d;

	for (int i = ean[u] + 1; i <= ean[u + 1]; i++)
	if (e[ea[i]].c > e[ea[i]].f)
	{
		x = e[ea[i]].b;
		if (h[x] + 1 == h[u])
		{
			d = min(nf, e[ea[i]].c - e[ea[i]].f);
			d = Argu(x, d);   z = 1;
			e[ea[i]].f += d;   nf -= d;
			if (h[ss] >= N || nf == 0)  return lf - nf;
		}
		else mh = min(mh, h[x]);
	}

	for (int i = ebn[u] + 1; i <= ebn[u + 1] && nf > 0; i++)
	if (e[eb[i]].f > 0)
	{
		x = e[eb[i]].a;
		if (h[x] + 1 == h[u])
		{
			d = min(nf, e[eb[i]].f);
			d = Argu(x, d);  z = 1;
			e[eb[i]].f -= d;  nf -= d;
			if (h[ss] >= N || nf == 0)  return lf - nf;
		}
		else mh = min(mh, h[x]);
	}

	if (z == 0)
	{
		if ((--nh[h[u]]) == 0) h[ss] = N;
		nh[h[u] = mh + 1] ++;
	}

	return lf - nf;
}

int MaxFlow()
{
	memset(ean, 0, sizeof(ean));
	memset(ebn, 0, sizeof(ebn));

	ss = 1;  tt = N;

	for (int i = 1; i <= M; i++)
	{
		ean[e[i].a] ++;
		ebn[e[i].b] ++;
		e[i].f = 0;
	}

	ean[N + 1] = M;   ebn[N + 1] = M;

	for (int i = 1; i <= N; i++)
	{
		ean[i] += ean[i - 1];
		ebn[i] += ebn[i - 1];
	}

	for (int i = 1; i <= M; i++)
	{
		ea[ean[e[i].a] --] = i;
		eb[ebn[e[i].b] --] = i;
	}

	memset(nh, 0, sizeof(nh));
	memset(h, 0, sizeof(h));
	nh[0] = N;
	int nMaxFlow = 0;
	while (h[ss] < N)
		nMaxFlow += Argu(ss, (1 << 30));

	return nMaxFlow;
}


set<string> lst[302];
set<string> allwords;

int Work()
{
	int sens;
	cin >> sens;
	string ss, se;
	getline(cin, ss);
	allwords.clear();
	for (int i = 0; i < sens; i++)
	{
		lst[i].clear();
		getline(cin, ss);
		stringstream ssin(ss);
		while (ssin >> se)
		{
			lst[i].insert(se);
			allwords.insert(se);
		}
	}

	vector<string> wdlist;
	for (string ww : allwords)
		wdlist.push_back(ww);
	
	N = 2 + sens + wdlist.size() * 2;
	M = 1;
	int base = 2 + sens, mmc = 1 << 20;
	AddEdge(1, 2, mmc);
	AddEdge(3, N, mmc);

	for (int i = 0; i < wdlist.size(); i++)
	{
		int aa = base + i, bb = base + i + wdlist.size();
		e[M].a = aa;  e[M].b = bb;  e[M].c = 1;  M++;
		//AddEdge(aa, bb, 1);
		for (int j = 0; j < sens; j++)
		{
			if (lst[j].find(wdlist[i]) != lst[j].end())
			{
				//AddEdge(2 + j, aa, mmc);
				//AddEdge(2 + j, bb, mmc);
				e[M].a = 2+j;  e[M].b = aa;  e[M].c = mmc;  M++;
				e[M].a = bb;  e[M].b = 2+j;  e[M].c = mmc;  M++;
			}
		}
	}
	M--;
	return MaxFlow();
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
		cout << "Case #" << t << ": " << Work() << endl;

	return 0;
}
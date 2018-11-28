#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

int ddx[4] = {0,  0, 1, -1};
int ddy[4] = {1, -1, 0,  0};

struct MaxFlow
{
	vector<map<int,i64> > c, d;
	int s, t;
	vector<int> w;

	i64 flow()
	{
		const i64 cInf = 1000000000000000000LL;
		int N = SZ(c);
		d.assign(N, map<int,i64>());
		i64 res = 0;
		while (true)
		{
			w.assign(N, 0);
			i64 flo = augment(s, cInf);
			if (!w[t]) break;
			res += flo;
		}
		return res;
	}

	i64 augment(int u, i64 flo)
	{
		w[u] = 1;
		deque<int> deq, pre;
		deque<i64> pot;
		deq.push_back(u);
		pre.push_back(-1);
		pot.push_back(flo);

		int r = 0;
		while (r < SZ(deq))
		{
			u = deq[r];
			flo = pot[r];
			if (u == t) break;

			for (map<int,i64>::reverse_iterator it = c[u].rbegin(); it != c[u].rend(); ++it)
			{
				int i = it->first;
				if (w[i]) continue;
				if (c[u][i] - d[u][i] > 0)
				{
					i64 tmp = min(flo, c[u][i] - d[u][i]);
					w[i] = 1;
					deq.push_back(i);
					pre.push_back(r);
					pot.push_back(tmp);
				}
			}

			++r;
		}

		if (u == t)
		{
			u = r;
			while (pre[u] != -1)
			{
				d[deq[pre[u]]][deq[u]] += flo;
				d[deq[u]][deq[pre[u]]] -= flo;
				u = pre[u];
			}
		}
		else
		{
			flo = 0;
		}

		return flo;
	}
};

void solve_case(int TN)
{
	int W, H, B;
	vi X0, Y0, X1, Y1;
	fin >> W >> H >> B;
	X0.resize(B);
	Y0.resize(B);
	X1.resize(B);
	Y1.resize(B);

	set<int> SXX, SYY;
	SXX.insert(0);
	SXX.insert(W);
	SYY.insert(0);
	SYY.insert(H);
	FOR(i, B)
	{
		fin >> X0[i] >> Y0[i] >> X1[i] >> Y1[i];
		SXX.insert(X0[i]);
		SXX.insert(X1[i]+1);
		SYY.insert(Y0[i]);
		SYY.insert(Y1[i]+1);
	}

	vi XX(ALL(SXX)), YY(ALL(SYY));

	{
		XX.clear();
		YY.clear();
		FOR(i, W+1) XX.push_back(i);
		FOR(i, H+1) YY.push_back(i);
	}

	int XN = SZ(XX)-1, YN = SZ(YY)-1;
	vvi C(XN, vi(YN, 0));
	FOR(i, B)
	{
		int sx = (int)(lower_bound(ALL(XX), X0[i]) - XX.begin());
		int sy = (int)(lower_bound(ALL(YY), Y0[i]) - YY.begin());
		for (int xi = sx; XX[xi] <= X1[i]; ++xi)
		{
			for (int yi = sy; YY[yi] <= Y1[i]; ++yi)
			{
				C[xi][yi] = 1;
			}
		}
	}

	MaxFlow maxflow;
	maxflow.s = 2*XN*YN;
	maxflow.t = 2*XN*YN+1;
	maxflow.c.assign(2*XN*YN+2, map<int,i64>());
	FOR(xi, XN)
	{
		FOR(yi, YN)
		{
			if (C[xi][yi]) continue;
			FOR(k, 4)
			{
				int nxi = xi + ddx[k];
				int nyi = yi + ddy[k];
				if (nxi < 0 || nxi >= XN || nyi < 0 || nyi >= YN) continue;
				if (C[nxi][nyi]) continue;
				int fl = xi == nxi ? XX[xi+1]-XX[xi] : YY[yi+1]-YY[yi];
				int u1 = xi * YN + yi + XN*YN;
				int u2 = nxi * YN + nyi;
				maxflow.c[u1][u2] = fl;
				maxflow.c[u2][u1] = 0;
			}
			int fl = max(XX[xi+1]-XX[xi], YY[yi+1]-YY[yi]);
			int u1 = xi * YN + yi;
			int u2 = xi * YN + yi + XN*YN;
			maxflow.c[u1][u2] = fl;
			maxflow.c[u2][u1] = 0;
		}
		int fl = XX[xi+1] - XX[xi];
		if (C[xi][0] == 0)
		{
			int u1 = maxflow.s;
			int u2 = xi * YN;
			maxflow.c[u1][u2] = fl;
			maxflow.c[u2][u1] = fl;
		}
		if (C[xi][YN-1] == 0)
		{
			int u1 = xi * YN + YN - 1 + XN*YN;
			int u2 = maxflow.t;
			maxflow.c[u1][u2] = fl;
			maxflow.c[u2][u1] = fl;
		}
	}

	i64 ans = maxflow.flow();

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("C.in"); 
	fout.open("C.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

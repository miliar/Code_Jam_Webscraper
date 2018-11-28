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

typedef vector<i64> vi;
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

// a - adjacency list
struct MaxMatching
{
	vector<vector<int> > a;
	bool found;
	vector<int> w, pr1, pr2;

	bool augment(int v)
	{
		w[v] = 1;
		deque<int> deq, pre;
		deq.push_back(v);
		pre.push_back(-1);

		int r = 0, last = -1;
		for (; r < SZ(deq); ++r)
		{
			int u = deq[r];
			FOR(ii, SZ(a[u]))
			{
				int i = a[u][ii];
				if (pr2[i] == -1)
				{
					last = i;
					break;
				}
				if (!w[pr2[i]])
				{
					deq.push_back(pr2[i]);
					pre.push_back(r);
					w[pr2[i]] = 1;
				}
			}
			if (last != -1) break;
		}
		if (last == -1) return false;
		for (; r != -1; r = pre[r])
		{
			pr2[last] = deq[r];
			swap(pr1[deq[r]], last);
		}
		return true;
	}

	int matching(int m)
	{
		int n = SZ(a);
		found = true;
		pr1.assign(n, -1);
		pr2.assign(m, -1);
		while (found)
		{
			found = false;
			w.assign(n, 0);
			FOR(i, n)
			{
				if (pr1[i] == -1 && augment(i))
				{
					found = true;
					break;
				}
			}
		}
		return n - (int)count(ALL(pr1), -1);
	}
};

void solve_case(int TN)
{
	int n;
	fin >> n;
	vs F(n), S(n);
	map<string,int> f2i, s2i;
	FOR(i, n)
	{
		fin >> F[i] >> S[i];
		f2i[F[i]] = 0;
		s2i[S[i]] = 0;
	}

	int f_cnt = 0;
	for (map<string,int>::iterator it = f2i.begin(); it != f2i.end(); it++)
		it->second = f_cnt++;

	int s_cnt = 0;
	for (map<string,int>::iterator it = s2i.begin(); it != s2i.end(); it++)
		it->second = s_cnt++;

	int n1 = SZ(f2i), n2 = SZ(s2i);
	MaxMatching mm;
	mm.a.assign(n1, vector<int>());
	FOR(i, n)
	{
		int k1 = f2i[F[i]];
		int k2 = s2i[S[i]];
		mm.a[k1].push_back(k2);
	}

	int m = mm.matching(n2);
	int ans = n - (n1 + n2 - m);

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

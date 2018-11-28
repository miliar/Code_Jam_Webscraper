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

void solve_case(int TN)
{
	int n, m;
	fin >> n >> m;
	vs Z(n);
	FOR(i, n) fin >> Z[i];
	vvi A(n, vi(n, 0));
	FOR(i, m)
	{
		int u, v;
		fin >> u >> v;
		--u, --v;
		A[u][v] = A[v][u] = 1;
	}

	int si = 0;
	FOR(i, n) if (Z[i] < Z[si]) si = i;

	string ans;
	deque<int> a;
	a.push_back(si);
	FOR(i, n) if (i != si) a.push_back(i);

	do 
	{
		deque<int> deq(1, a[0]);
		string tmp = Z[a[0]];
		FORD(i, 1, n-1)
		{
			while (!deq.empty())
			{
				int u = deq.back();
				int v = a[i];
				if (A[u][v])
				{
					deq.push_back(v);
					tmp += Z[v];
					break;
				}
				deq.pop_back();
			}
			if (deq.empty()) break;
		}
		if (!deq.empty() && (ans.empty() || ans > tmp))
		{
			ans = tmp;
		}
	} while(next_permutation(a.begin()+1, a.end()));

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

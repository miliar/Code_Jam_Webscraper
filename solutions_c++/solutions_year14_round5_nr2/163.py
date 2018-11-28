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

vvi f;
int P, Q, N;
vector<int> H, B;
vi G;

i64 rec(int m, int k)
{
	if (k >= N)	return 0;
	i64 & r = f[m][k];
	if (r > -1) return r;
	
	r = 0;

	// not to kill
	int tower_moves = H[k] / Q;
	int md = H[k] % Q;
	if (md != 0) ++tower_moves;
	r = max(r, rec(m+tower_moves, k+1));

	// kill
	if (m + B[k] >= 0)
	{
		r = max(r, rec(m + B[k], k+1) + G[k]);
	}

	return r;
}

void solve_case(int TN)
{
	fin >> P >> Q >> N;
	H.assign(N, 0);
	G.assign(N, 0);
	FOR(i, N) fin >> H[i] >> G[i];

	B.assign(N, 0);
	FOR(i, N)
	{
		int md = H[i] % Q;
		int mv = H[i] / Q;
		if (md == 0)
		{
			--mv;
			md = Q;
		}
		int mym = md / P;
		if (md % P != 0) ++mym;
		B[i] = mv - mym;
	}

	f.assign(100000, vi(N+1, -1));
	i64 ans = rec(1, 0);

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("B.in"); 
	fout.open("B.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

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
	int nA, nW, n;
	string A, W;
	fin >> nA >> nW >> n;
	fin >> A >> W;

 	int P = 0;
 	FORD(i, 1, nW-1) if (W.substr(i) == W.substr(0, nW-i))
 	{
 		P = nW-i;
 		break;
 	}

	int M = 1 + (n - nW) / (nW - P);

	vi C(256, 0);
	FOR(i, nA) C[A[i]]++;

	ld ans = n - nW + 1;
	FOR(i, nW) 
	{
		ans *= C[W[i]] / (ld)nA;
		if (C[W[i]] == 0)
			M = 0;
	}

	ans = M - ans;

	fout << fixed << setprecision(8) << "Case #" << TN << ": " << ans << endl;
	cout << fixed << setprecision(8) << "Case #" << TN << ": " << ans << endl;
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

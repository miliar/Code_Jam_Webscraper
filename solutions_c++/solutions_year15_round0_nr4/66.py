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

bool solve(int X, int N, int M)
{
	if (N * M % X != 0) return true;
	if (X > M) return true;
	if ((X+1) / 2 > N) return true;
	if (X >= 7) return true;
	if (X <= 3) return false;
	if (X == 4)
	{
		if (N > 2) return false;
		return true;
	}
	if (X == 5)
	{
		if (N > 3) return false;
		if (M == 5) return true;
		return false;
	}
	// X == 6
	if (N > 3) return false;
	return true;
}

void solve_case(int TN)
{
	int X, N, M;
	fin >> X >> N >> M;
	if (N > M) swap(N, M);

	string ans = solve(X, N, M) ? "RICHARD" : "GABRIEL"; 

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("D.in"); 
	fout.open("D.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

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


void solve_case(int TN)
{
	int N;
	i64 p, q, r, s;
	fin >> N >> p >> q >> r >> s;
	vi A(N+1), S(N+1, 0);
	FORD(i, 1, N)
	{
		A[i] = ((i-1) * p + q) % r + s;
		S[i] = S[i-1] + A[i];
	}

	i64 ans = S[N];
	FORD(i, 1, N)
	{
		int a = i, b = N;
		while (a+1 < b)
		{
			int m = (a+b)/2;
			if (S[m]-S[i-1] < S[N]-S[m])
				a = m;
			else
				b = m;
		}
		ans = min( ans, max( S[N]-S[a], max(S[i-1], S[a]-S[i-1]) ) );
		ans = min( ans, max( S[N]-S[b], max(S[i-1], S[b]-S[i-1]) ) );
	}

	ld a1 = (ld)(S[N] - ans) / (ld)S[N];
	fout << fixed << setprecision(12) << "Case #" << TN << ": " << a1 << endl;
	cout << fixed << setprecision(12) << "Case #" << TN << ": " << a1 << endl;
}

int main()
{
	fin.open("A.in"); 
	fout.open("A.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

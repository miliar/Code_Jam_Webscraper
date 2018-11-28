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

int bitcnt(i64 msk)
{
	int cnt = 0;
	while (msk) ++cnt, msk &= msk-1;
	return cnt;
}

void solve_case(int TN)
{
	int n, k;
	fin >> n >> k;
	vd P(n);
	FOR(i, n) fin >> P[i];

	ld ans = 0;
	FOR(msk, 1<<n)
	{
		if (bitcnt(msk) != k) continue;
		vd Q;
		FOR(i, n) if (msk & (1<<i)) Q.push_back(P[i]);
		vvd F(k+1, vd(k+1, 0));
		F[0][0] = 1;
		FORD(i, 1, k)
		{
			F[i][0] = F[i-1][0] * (1 - Q[i-1]);
			FORD(j, 1, k)
			{
				F[i][j] = F[i-1][j] * (1 - Q[i-1]) + F[i-1][j-1] * Q[i-1];
			}
		}
		ans = max(ans, F[k][k/2]);
	}

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

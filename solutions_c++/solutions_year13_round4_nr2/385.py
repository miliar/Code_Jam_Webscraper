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
	i64 N, P;
	fin >> N >> P;

	i64 PN = 1LL << N;
	i64 ans1 = PN-1, ans2 = PN-1;

	if (P < PN)
	{
		i64 a = 0, b = PN-1;
		while (a+1 < b)
		{
			i64 m = (a + b) / 2;
			i64 lc = PN - m, pos = PN;
			while (lc > 1)
			{
				lc /= 2;
				pos /= 2;
			}
			if (pos <= P)
				a = m;
			else
				b = m;
		}
		ans2 = a;

		a = 0, b = PN-1;
		while (a+1 < b)
		{
			i64 m = (a + b) / 2;
			i64 lc = m + 1, pos = 0, s = PN;
			while (lc > 1)
			{
				lc /= 2;
				s /= 2;
				pos += s;
			}
			if (pos >= P)
				b = m;
			else
				a = m;
		}
		ans1 = a;
	}

	fout << "Case #" << TN << ": " << ans1 << " " << ans2 << endl;
	cout << "Case #" << TN << ": " << ans1 << " " << ans2 << endl;
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

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
	int K, C, S;
	fin >> K >> C >> S;

	if (S < (K + C - 1) / C)
	{
		fout << "Case #" << TN << ": IMPOSSIBLE\n";
		cout << "Case #" << TN << ": IMPOSSIBLE\n";
		return;
	}


	fout << "Case #" << TN << ":";
	cout << "Case #" << TN << ":";

	if (K == 1)
	{
		fout << " 1\n";
		cout << " 1\n";
		return;
	}

	i64 pw = 1;
	FOR(i, C-1) pw *= K;
	for (int i = 0, d = 0; i < S && d < K; i++)
	{
		i64 idx = 0, kc = pw;
		FOR(j, C)
		{
			idx += min(d, K-1) * kc;
			d++;
			kc /= K;
		}
		idx++;
		fout << ' ' << idx;
		cout << ' ' << idx;
	}
	fout << endl;
	cout << endl;
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

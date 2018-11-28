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
	vvi a(n, vi(m));
	FOR(i, n) FOR(j, m) fin >> a[i][j];
	
	string ans = "YES";
	FOR(i, n) if (ans == "YES") FOR(j, m)
	{
		int fu = 1, fd = 1, fl = 1, fr = 1; 
		FOR(k, n)
		{
			if (k < i && a[k][j] > a[i][j]) fu = 0;
			if (k > i && a[k][j] > a[i][j]) fd = 0;
		}
		FOR(k, m)
		{
			if (k < j && a[i][k] > a[i][j]) fl = 0;
			if (k > j && a[i][k] > a[i][j]) fr = 0;
		}
		if (fu + fd < 2 && fl + fr < 2)
		{
			ans = "NO";
			break;
		}
	}

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

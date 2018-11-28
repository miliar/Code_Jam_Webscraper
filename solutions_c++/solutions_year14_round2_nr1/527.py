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

string tob(string a)
{
	string r;
	r += a[0];
	FOR(i, LEN(a)-1)
		if (a[i] != a[i+1])
			r += a[i+1];
	return r;
}

void solve_case(int TN)
{
	int n;
	fin >> n;
	vs A(n);
	FOR(i, n) fin >> A[i];

	bool can = true;
	FOR(i, n-1)
		if (tob(A[i]) != tob(A[i+1]))
			can = false;

	if (!can)
	{
		fout << "Case #" << TN << ": Fegla Won\n";
		cout << "Case #" << TN << ": Fegla Won\n";
		return;
	}

	int ans = 0;
	while (!A[0].empty())
	{
		vi c(n, 0);
		char ch = A[0][0];
		FOR(i, n)
		{
			while (!A[i].empty() && A[i][0] == ch)
			{
				++c[i];
				A[i].erase(0, 1);
			}
		}
		sort(ALL(c));
		FOR(i, n) ans += abs(c[i]-c[n/2]);
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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

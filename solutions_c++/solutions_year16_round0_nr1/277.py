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

void n2arr(i64 n, vi& a)
{
	a.clear();
	if (n == 0) a.push_back(0);
	while (n > 0)
	{
		a.push_back(n%10);
		n /= 10;
	}
}

void solve_case(int TN)
{
	i64 n;
	fin >> n;

	if (n == 0)
	{
		fout << "Case #" << TN << ": INSOMNIA\n";
		cout << "Case #" << TN << ": INSOMNIA\n";
		return;
	}
	
	i64 msk = 0, ns = 0;
	vi a;
	while (msk < (1LL << 10) - 1)
	{
		ns += n;
		n2arr(ns, a);
		FOR(i, SZ(a))
			msk |= 1LL << a[i];
	}

	fout << "Case #" << TN << ": " << ns << endl;
	cout << "Case #" << TN << ": " << ns << endl;
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

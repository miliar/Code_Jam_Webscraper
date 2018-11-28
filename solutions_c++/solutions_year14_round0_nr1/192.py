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
	int k, x, c1 = 0, c2 = 0;
	fin >> k;
	FOR(i, 4) FOR(j, 4)
	{
		fin >> x;
		if (i+1 == k) c1 |= 1<<x;
	}
	fin >> k;
	FOR(i, 4) FOR(j, 4)
	{
		fin >> x;
		if (i+1 == k) c2 |= 1<<x;
	}
	vector<int> r;
	FORD(i, 1, 16) 
		if ((c1 & c2) & (1<<i))
			r.push_back(i);
	if (r.empty())
	{
		fout << "Case #" << TN << ": Volunteer cheated!\n";
		cout << "Case #" << TN << ": Volunteer cheated!\n";
	}
	else if (SZ(r) == 1)
	{
		fout << "Case #" << TN << ": " << r[0] << endl;
		cout << "Case #" << TN << ": " << r[0] << endl;
	}
	else
	{
		fout << "Case #" << TN << ": Bad magician!\n";
		cout << "Case #" << TN << ": Bad magician!\n";
	}
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

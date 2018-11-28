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

int dwar(deque<ld> N, deque<ld> K)
{
	int r = 0;
	while (!N.empty())
	{
		if (N[0] < K[0])
		{
			N.pop_front();
			K.pop_back();
		}
		else
		{
			++r;
			N.pop_front();
			K.pop_front();
		}
	}
	return r;
}

int war(deque<ld> N, deque<ld> K)
{
	int r = 0;
	FORR(i, 0, SZ(N)-1)
	{
		if (N[i] < K.back())
			K.pop_back();
	}
	return SZ(K);
}

void solve_case(int TN)
{
	int n;
	fin >> n;
	deque<ld> N(n), K(n);
	FOR(i, n) fin >> N[i];
	FOR(i, n) fin >> K[i];
	sort(ALL(N));
	sort(ALL(K));
	fout << "Case #" << TN << ": " << dwar(N, K) << " " << war(N, K) << endl;
	cout << "Case #" << TN << ": " << dwar(N, K) << " " << war(N, K) << endl;
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

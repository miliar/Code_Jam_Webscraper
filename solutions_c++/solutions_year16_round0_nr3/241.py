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
#include <bitset>

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

vector<char> isP;
vi Pr;

void Eratosthenes(int n, vector<char>& p)
{
	p.assign(n+1, 1);
	p[0] = p[1] = 0;
	for (int i = 4; i <= n; i += 2) p[i] = 0;
	for (int i = 3; i * i <= n; i += 2)
	{
		if (!p[i]) continue;
		int ii = i+i;
		for (int j = i+ii; j <= n; j += ii)
			p[j] = 0;
	}
}

void primes(int n, vi& pr)
{
	pr.clear();
	Eratosthenes(n, isP);
	if (n > 1) pr.push_back(2);
	for (int i = 3; i <= n; i += 2) 
		if (isP[i]) pr.push_back(i);
}

int compX(i64 n, int m, int b)
{
	FOR(i, SZ(Pr))
	{
		int r = 0;
		FORR(j, 0, m-1)
		{
			r = r * b + (int)((n >> j) & 1);
			r %= Pr[i];
		}
		if (r == 0)
			return Pr[i];
	}
	return 0;
}

void solve_case(int TN)
{
	int m, k;
	fin >> m >> k;

	fout << "Case #" << TN << ":\n";
	cout << "Case #" << TN << ":\n";

	i64 n = (1LL << (m - 1)) + 1;
	for (int i = 0; i < k; n += 2)
	{
		vi Q;
		FORD(b, 2, 10)
		{
			Q.push_back(compX(n, m, b));
			if (Q.back() == 0)
			{
				Q.clear();
				break;
			}
		}
		if (!Q.empty())
		{
			bitset<32> x(n);
			fout << x;
			cout << x;
			FOR(j, SZ(Q))
			{
				fout << ' ' << Q[j];
				cout << ' ' << Q[j];
			}
			fout << endl;
			cout << endl;
			i++;
		}
	}
}

int main()
{
	primes(100, Pr);

	fin.open("C.in"); 
	fout.open("C.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

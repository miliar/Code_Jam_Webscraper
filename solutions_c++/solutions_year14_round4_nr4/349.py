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

vs A;
vector<vs> P;
int n, m;
int gans, gcnt;

int rec(vs & S, int a, int b, int k)
{
	int r = 0, pi = a;
	FORD(i, a, b)
	{
		if (k >= LEN(S[i]))
		{
			pi = i+1;
			continue;
		}
		if (S[i][k] != S[pi][k])
		{
			r += 1 + rec(S, pi, i-1, k+1);
			pi = i;
		}
	}
	if (pi <= b)
		r += 1 + rec(S, pi, b, k+1);
	return r;
}

void divide(int r, int k, int msk, int st)
{
	if (k > r || st >= m || 0 == k && r > 0) return;
	if (k == 0 && r == 0)
	{
		int tmp = 0;
		FOR(i, n) tmp += 1 + rec(P[i+1], 0, SZ(P[i+1])-1, 0);
		if (tmp > gans)
			gans = tmp,	gcnt = 1;
		else if (tmp == gans)
			++gcnt;
		return;
	}
	FORD(i, st, m-1)
	{
		if (~msk & (1<<i)) continue;
		P[k].push_back(A[i]);
		divide(r-1, k, msk-(1<<i), i+1);
		divide(r-1, k-1, msk-(1<<i), 0);
		P[k].pop_back();
	}
}

void solve_case(int TN)
{
	fin >> m >> n;
	A.assign(m, "");
	FOR(i, m) fin >> A[i];
	sort(ALL(A));
	
	gans = 0;
	gcnt = 0;
	P.assign(n+1, vs());
	divide(m, n, (1<<m)-1, 0);

	fout << "Case #" << TN << ": " << gans << " " << gcnt << endl;
	cout << "Case #" << TN << ": " << gans << " " << gcnt << endl;
}

int main()
{
	fin.open("D1.in"); 
	fout.open("D1.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

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

int Tr[8][8] = {
	{0, 1, 2, 3,   0, 0, 0, 0},
	{1, 4, 3, 6,   0, 0, 0, 0},
	{2, 7, 4, 1,   0, 0, 0, 0},
	{3, 2, 5, 4,   0, 0, 0, 0},

	{0, 0, 0, 0,   0, 0, 0, 0},
	{0, 0, 0, 0,   0, 0, 0, 0},
	{0, 0, 0, 0,   0, 0, 0, 0},
	{0, 0, 0, 0,   0, 0, 0, 0}
};


void solve_case(int TN)
{
	int L;
	i64 k;
	string s;
	fin >> L >> k >> s;
	vi a(L);
	int Z = 0;
	FOR(i, L) 
	{
		a[i] = s[i] == 'i' ? 1 : s[i] == 'j' ? 2 : 3;
		Z = Tr[Z][a[i]];
	}

	int ZZ = 0;
	FOR(i, k % 8) ZZ = Tr[ZZ][Z];

	if (Tr[1][Tr[2][3]] != ZZ)
	{
		fout << "Case #" << TN << ": NO\n";
		cout << "Case #" << TN << ": NO\n";
		return;
	}
	
	bool yes = false;
	int Q1 = 0;
	FOR(li, 4)
	{
		if (li >= k) break;
		int Q2 = 0;
		FOR(ri, 4)
		{
			if (li + ri >= k) break;
			int W1 = 0;
			FOR(lj, L)
			{
				if (li + lj == 0) { W1 = Tr[W1][a[lj]]; continue; }
				if (Tr[Q1][W1] == 1)
				{
					int W2 = 0;
					FOR(rj, L)
					{
						if (ri + rj == 0) { W2 = Tr[a[L-1-rj]][W2]; continue; }
						if (lj + rj >= L && li + ri == k-1) break;
						if (Tr[W2][Q2] == 3)
						{
							yes = true;
							break;
						}
						W2 = Tr[a[L-1-rj]][W2];
					}
				}
				if (yes) break;
				W1 = Tr[W1][a[lj]];
			}
			if (yes) break;
			Q2 = Tr[Z][Q2];
		}
		if (yes) break;
		Q1 = Tr[Q1][Z];
	}

	string ans = yes ? "YES" : "NO";

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	FOR(i, 4) FOR(j, 4)
	{
		Tr[i+4][j] = (4 + Tr[i][j]) % 8;
		Tr[i][j+4] = (4 + Tr[i][j]) % 8;
		Tr[i+4][j+4] = Tr[i][j];
	}

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

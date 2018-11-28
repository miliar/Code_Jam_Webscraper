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

vi CurK, KType;
vvi Keys;
vi F;
int K, N;

int rec(int msk)
{
	if (msk == 0) return 1;
	if (F[msk] != -1) return F[msk];
	FOR(i, N)
	{
		if ((msk & (1<<i)) && CurK[KType[i]] > 0)
		{
			--CurK[KType[i]];
			FOR(j, SZ(Keys[i])) ++CurK[Keys[i][j]];
			int r = rec(msk^(1<<i));
			++CurK[KType[i]];
			FOR(j, SZ(Keys[i])) --CurK[Keys[i][j]];
			if (r == 1) return F[msk] = 1;
		}
	}
	return F[msk] = 0;
}

void solve_case(int TN)
{
	fin >> K >> N;
	CurK.assign(201, 0);
	FOR(i, K) 
	{
		int kk;
		fin >> kk;
		++CurK[kk];
	}
	Keys.assign(N, vi());
	KType.resize(N);
	FOR(i, N)
	{
		int L;
		fin >> KType[i] >> L;
		Keys[i].resize(L);
		FOR(j, L) fin >> Keys[i][j];
	}

	F.assign(1<<N, -1);
	if (rec((1<<N)-1) == 0)
	{
		fout << "Case #" << TN << ": IMPOSSIBLE" << endl;
		cout << "Case #" << TN << ": IMPOSSIBLE" << endl;
		return;
	}

	vi ans;
	int msk = (1<<N)-1;
	FOR(t, N)
	{
		FOR(i, N) 
		{
			if ((msk & (1<<i)) && CurK[KType[i]] > 0)
			{
				--CurK[KType[i]];
				FOR(j, SZ(Keys[i])) ++CurK[Keys[i][j]];
				int r = rec(msk^(1<<i));
				if (r == 1)
				{
					msk ^= (1<<i);
					ans.push_back(i+1);
					break;
				}
				++CurK[KType[i]];
				FOR(j, SZ(Keys[i])) --CurK[Keys[i][j]];
			}
		}
	}

	fout << "Case #" << TN << ":";
	cout << "Case #" << TN << ":";
	FOR(i, N)
	{
		fout << " " << ans[i];
		cout << " " << ans[i];
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

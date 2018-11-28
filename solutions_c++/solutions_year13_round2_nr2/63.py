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
	int N, X, Y;
	fin >> N >> X >> Y;
	X = abs(X);

	map<int,int> Cnt;
	Cnt[1] = 1;
	int r = 1, s = 1;
	while (s <= N)
	{
		s += r * 4 + 1;
		++r;
		Cnt[s] = r;
	}

	ld ans = 0.0;
	if (Cnt.count(N))
	{
		if (X + Y < 2 * Cnt[N])
			ans = 1.0;
	}
	else
	{
		map<int,int>::iterator it = Cnt.lower_bound(N);
		if (X + Y < 2 * (it->second - 1))
		{
			ans = 1.0;
		}
		else if (X + Y >= 2 * it->second || X == 0)
		{
			ans = 0.0;
		}
		else
		{
			--it;
			int R = N - it->first;
			int V = 2 * it->second;
			vvd F(V+1, vd(V+1, 0.0));
			F[0][0] = 1.0;
			FORD(i, 0, V) FORD(j, 0, V) if (i + j <= R)
			{
				if (i + j == R && Y < j)
				{
					ans += F[i][j];
				}

				if (i < V && j < V)
				{
					F[i+1][j] += F[i][j] * 0.5;
					F[i][j+1] += F[i][j] * 0.5;
				}
				else if (i < V)
				{
					F[i+1][j] += F[i][j];
				}
				else if (j < V)
				{
					F[i][j+1] += F[i][j];
				}
			}
		}
	}

	fout << fixed << setprecision(9) << "Case #" << TN << ": " << ans << endl;
	cout << fixed << setprecision(9) << "Case #" << TN << ": " << ans << endl;
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

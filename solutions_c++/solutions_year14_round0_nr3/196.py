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
	int R, C, M;
	fin >> R >> C >> M;

	bool swappped = false;
	if (R > C) { swappped = true; swap(R, C); }
	int K = R * C - M;

	vs ans;

	if (R == 1)
	{
		string s(C, '*');
		FOR(i, K) s[i] = '.';
		s[0] = 'c';
		ans.push_back(s);
	}
	else if (R == 2)
	{
		if (K == 1 || K > 2 && K % 2 == 0)
		{
			string s(C, '*');
			FOR(i, K/2) s[i] = '.';
			ans.push_back(s);
			s[0] = 'c';
			ans.push_back(s);
		}
	}
	else
	{
		if (K == 1 || K == 4 || K == 6 || K >= 8)
		{
			ans.assign(R, string(C, '*'));
			int D = (int)sqrt(K-0.001) + 1;
			D = min(D, R);
			int i = 0;
			for (; K >= D; i++)
			{
				FOR(j, D)
				{
					--K;
					ans[j][i] = '.';
				}
			}
			if (K == 1)
			{
				ans[D-1][i-1] = '*';
				ans[0][i] = ans[1][i] = '.';
			}
			else
			{
				FOR(j, K) ans[j][i] = '.';
			}
			ans[0][0] = 'c';
		}
	}

	if (ans.empty())
	{
		fout << "Case #" << TN << ": \nImpossible\n";
		cout << "Case #" << TN << ": \nImpossible\n";
	}
	else
	{
		vs ansT(C, string(R, 0));
		FOR(i, R) FOR(j, C) ansT[j][i] = ans[i][j];
		if (swappped) ans = ansT;
		fout << "Case #" << TN << ":\n";
		cout << "Case #" << TN << ":\n";
		FOR(i, SZ(ans))
		{
			FOR(j, LEN(ans[0]))
			{
				fout << ans[i][j];
				cout << ans[i][j];
			}
			fout << endl;
			cout << endl;
		}
	}
}

int main()
{
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

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

const int BUFN = 12000;
char buf[BUFN];

void solve_case(int TN)
{
	int n;
	fin >> n;

	fin.getline(buf, BUFN);

	map<string,int> w2id;
	vvi A(n);
	int idN = 0;
	vi L;
	FOR(i, n)
	{
		fin.getline(buf, BUFN);
		iss istr(buf);
		string s;
		while (istr >> s)
		{
			int idx = idN;
			if (w2id.count(s))
			{
				idx = w2id[s];
			}
			else
			{
				L.push_back(0);
				w2id[s] = idN;
				idN++;
			}
			A[i].push_back(idx);
			if (i == 0) L[idx] |= 1;
			if (i == 1) L[idx] |= 2;
		}
	}

	int ans = (int)count(ALL(L), 3);
	bool t1 = true;

	if (n > 2)
	{
		FOR(msk, 1<<n)
		{
			if (msk & 3) continue;
			vi L1 = L;
			FORD(i, 2, n-1)
			{
				FOR(j, SZ(A[i]))
				{
					if (msk & (1<<i))
					{
						L1[A[i][j]] |= 1;
					}
					else
					{
						L1[A[i][j]] |= 2;
					}
				}
			}
			int tmp = (int)count(ALL(L1), 3);
			if (t1 || tmp < ans)
				ans = tmp;
			t1 = false;
		}
	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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

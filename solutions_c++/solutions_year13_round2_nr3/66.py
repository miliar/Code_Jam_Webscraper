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

set<string> D;

pii match(const string & a, const string & b, int pr)
{
	int m = LEN(a), prev = pr, cnt = 0;
	FOR(i, m)
	{
		if (a[i] != b[i])
		{
			if (i-prev < 5) return pii(-1, -1);
			++cnt;
			prev = i;
		}
	}
	return pii(cnt, min(m-1-prev, 4));
}

void solve_case(int TN)
{
	string S;
	fin >> S;
	int N = LEN(S);

	const int inf = 9999;
	vvi F(N, vi(5, inf));
	for (set<string>::iterator it = D.begin(); it != D.end(); ++it)
	{
		string & d = *it;
		int M = LEN(d);
		if (M > N) continue;
		pii p = match(S.substr(0, M), d, -5);
		if (p.first == -1) continue;
		F[M-1][p.second] = min(F[M-1][p.second], p.first);
	}

	FORD(i, 0, N-2)
	{
		FOR(k, 5)
		{
			if (F[i][k] == inf) continue;
			string f4 = S.substr(i+1, 4);
			FOR(j, LEN(f4)) FORD(c, 'a', 'z')
			{
				string g4 = f4;
				g4[j] = c;
				set<string>::iterator it = D.lower_bound(g4);
				for (; it != D.end(); ++it)
				{
					string & d = *it;
					int M = LEN(d);
					int B = min(LEN(g4), M);
					if (g4.substr(0, B) != d.substr(0, B)) break;
					if (M > N-1-i) continue;
					pii p = match(S.substr(i+1, M), d, -k-1);
					if (p.first == -1) continue;
					F[i+M][p.second] = min(F[i+M][p.second], p.first + F[i][k]);
				}
				FORD(q, 1, LEN(g4)-1)
				{
					it = D.find(g4.substr(0, q));
					if (it == D.end()) continue;
					string & d = *it;
					int M = LEN(d);
					int B = min(LEN(g4), M);
					if (g4.substr(0, B) != d.substr(0, B)) continue;
					if (M > N-1-i) continue;
					pii p = match(S.substr(i+1, M), d, -k-1);
					if (p.first == -1) continue;
					F[i+M][p.second] = min(F[i+M][p.second], p.first + F[i][k]);
				}
			}
		}
	}

	int ans = inf;
	FOR(k, 5) ans = min(ans, F[N-1][k]);
	
	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	ifstream fdict("garbled_email_dictionary.txt");
	string s;
	while (fdict >> s) D.insert(s);
	fdict.close();

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

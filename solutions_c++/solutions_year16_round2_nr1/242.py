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

string digs[10] = {
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

pii getUni(const vi & used)
{
	vi cnt(26, 0);
	FOR(i, 10)
	{
		if (used[i]) continue;
		string s = digs[i];
		FOR(j, LEN(s))
			++cnt[s[j]-'A'];
	}
	int k = -1;
	FOR(i, 26)
		if (cnt[i] == 1)
			k = i;
	FOR(i, 10)
	{
		if (used[i]) continue;
		if (count(ALL(digs[i]), k+'A'))
			return pii(i, k);
	}
	return pii(0, 0);
}

void solve_case(int TN)
{
	string s;
	fin >> s;
	vi cnt(26, 0);
	FOR(i, LEN(s)) ++cnt[s[i]-'A'];
	vi used(10, 0);
	string ans;
	FOR(i, 10)
	{
		pii k = getUni(used);
		used[k.first] = 1;
		int t = cnt[k.second];
		FOR(j, t)
		{
			ans += (char)(k.first+'0');
			FOR(p, LEN(digs[k.first]))
				--cnt[digs[k.first][p]-'A'];
		}
	}

	sort(ALL(ans));

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
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

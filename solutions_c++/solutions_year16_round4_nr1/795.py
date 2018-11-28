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

vs P, R, S;

void getPRS(string d, int & p1, int & r1, int & s1)
{
	p1 = 0, r1 = 0, s1 = 0;
	FOR(i, LEN(d))
	{
		if (d[i] == 'P') ++p1;
		if (d[i] == 'R') ++r1;
		if (d[i] == 'S') ++s1;
	}
}

void upd(string d, string & w)
{
	if (w.empty() || d < w)
		w = d;
}

bool check(string d)
{
	while (LEN(d) > 1)
	{
		string z;
		for (int i = 0; i < LEN(d); i += 2)
		{
			if (d[i] == d[i+1]) return false;
			if (d[i] > d[i+1]) swap(d[i], d[i+1]);
			if (d[i] == 'P' && d[i+1] == 'R') z += 'P';
			if (d[i] == 'P' && d[i+1] == 'S') z += 'S';
			if (d[i] == 'R' && d[i+1] == 'S') z += 'R';
		}
		d = z;
	}
	return true;
}

void solve_case(int TN)
{
	int n, p, r, s;
	fin >> n >> r >> p >> s;

	string ans;
	int p1, r1, s1;

	getPRS(P[n], p1, r1, s1);
	if (p == p1 && r == r1 && s == s1) 
		upd(P[n], ans);

	getPRS(R[n], p1, r1, s1);
	if (p == p1 && r == r1 && s == s1) 
		upd(R[n], ans);

	getPRS(S[n], p1, r1, s1);
	if (p == p1 && r == r1 && s == s1) 
		upd(S[n], ans);

	if (ans.empty())
		ans = "IMPOSSIBLE";
	
// 	{
// 		string ans2;
// 		int m = p + r + s;
// 		string h;
// 		FOR(i, p) h += 'P';
// 		FOR(i, r) h += 'R';
// 		FOR(i, s) h += 'S';
// 		vector<int> a(m);
// 		FOR(i, m) a[i] = i;
// 		do 
// 		{
// 			string q;
// 			FOR(i, m) q += h[a[i]];
// 			if (check(q))
// 				upd(q, ans2);
// 		} while(next_permutation(ALL(a)));
// 
// 		if (ans2.empty())
// 			ans2 = "IMPOSSIBLE";
// 
// 		if (ans != ans2)
// 		{
// 			cout << "error\n";
// 		}
// 	}

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("A.in"); 
	fout.open("A.out");

	P.resize(13);
	R.resize(13);
	S.resize(13);
	P[0] = "P";
	R[0] = "R";
	S[0] = "S";
	FORD(i, 1, 12)
	{
		if (P[i-1] < R[i-1])
			P[i] = P[i-1] + R[i-1];
		else
			P[i] = R[i-1] + P[i-1];

		if (R[i-1] < S[i-1])
			R[i] = R[i-1] + S[i-1];
		else
			R[i] = S[i-1] + R[i-1];

		if (S[i-1] < P[i-1])
			S[i] = S[i-1] + P[i-1];
		else
			S[i] = P[i-1] + S[i-1];
	}

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}

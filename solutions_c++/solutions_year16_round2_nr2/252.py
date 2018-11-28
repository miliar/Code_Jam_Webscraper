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
typedef vector<vs> vvs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

vs FC, FJ;
vi F;
string C, J;

void rec(int i)
{
	if (F[i] != -1) return;
	if (i == LEN(C))
	{
		F[i] = 0;
		return;
	}
	F[i] = (i64)1e18;
	FOR(d1, 10)
	{
		char c1 = C[i] == '?' ? d1 : C[i]-'0';
		FOR(d2, 10)
		{
			char c2 = J[i] == '?' ? d2 : J[i]-'0';
			if (c1 == c2)
			{
				rec(i+1);
				if (F[i+1] < F[i])
				{
					F[i] = F[i+1];
					FC[i] = (char)(c1+'0') + FC[i+1];
					FJ[i] = (char)(c2+'0') + FJ[i+1];
				}
			}
			else if (c1 < c2)
			{
				i64 n1 = c1, n2 = c2;
				string t1(1, c1+'0'), t2(1, c2+'0');
				FORD(j, i+1, LEN(C)-1)
				{
					t1 += (C[j] == '?' ? '9' : C[j]);
					t2 += (J[j] == '?' ? '0' : J[j]);
					n1 = n1 * 10 + (C[j] == '?' ? 9 : C[j]-'0');
					n2 = n2 * 10 + (J[j] == '?' ? 0 : J[j]-'0');
				}
				if (n2 - n1 < F[i])
				{
					F[i] = n2 - n1;
					FC[i] = t1;
					FJ[i] = t2;
				}
			}
			else
			{
				i64 n1 = c1, n2 = c2;
				string t1(1, c1+'0'), t2(1, c2+'0');
				FORD(j, i+1, LEN(C)-1)
				{
					t1 += (C[j] == '?' ? '0' : C[j]);
					t2 += (J[j] == '?' ? '9' : J[j]);
					n1 = n1 * 10 + (C[j] == '?' ? 0 : C[j]-'0');
					n2 = n2 * 10 + (J[j] == '?' ? 9 : J[j]-'0');
				}
				if (n1 - n2 < F[i])
				{
					F[i] = n1 - n2;
					FC[i] = t1;
					FJ[i] = t2;
				}
			}
		}
	}
}

bool match(string s, string pat)
{
	FOR(i, LEN(s))
		if (pat[i] != '?' && pat[i] != s[i])
			return false;
	return true;
}

void solve_case(int TN)
{
	fin >> C >> J;
	FC.assign(LEN(C) + 1, "");
	FJ.assign(LEN(C) + 1, "");
	F.assign(LEN(C) + 1, -1);
	rec(0);

// 	int m = LEN(C);
// 	int lm = 1;
// 	FOR(i, m) lm *= 10;
// 	int df = 10000;
// 	string r1, r2;
// 	FOR(i, lm)
// 	{
// 		oss o1;
// 		o1 << setw(m) << setfill('0') << i;
// 		string s1 = o1.str();
// 		if (!match(s1, C)) continue;
// 		FOR(j, lm)
// 		{
// 			oss o2;
// 			o2 << setw(m) << setfill('0') << j;
// 			string s2 = o2.str();
// 			if (!match(s2, J)) continue;
// 			if (abs(i-j) < df || abs(i-j) == df && s1 < r1 || abs(i-j) == df && s1 == r1 && s2 < r2)
// 			{
// 				df = abs(i-j);
// 				r1 = s1;
// 				r2 = s2;
// 			}
// 		}
// 	}
// 
// 	if (F[0] != df || FC[0] != r1 || FJ[0] != r2)
// 	{
// 		cout << "err\n";
// 	}
// 
	fout << "Case #" << TN << ": " << FC[0] << " " << FJ[0] << endl;
	cout << "Case #" << TN << ": " << FC[0] << " " << FJ[0] << endl;
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

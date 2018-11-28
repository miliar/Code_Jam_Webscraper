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

i64 str2i(string s)
{
	i64 r = 0;
	FOR(i, LEN(s))
		r = r * 10 + s[i]-'0';
	return r;
}

i64 pow10(int k)
{
	i64 r = 1;
	FOR(i, k) r *= 10;
	return r;
}

void solve_case(int TN)
{
	string s;
	fin >> s;
	string d = s;
	int m = LEN(d);
	i64 ans = 0;
	while ((m = LEN(d)) > 1)
	{
		if (d[0] == '1' && d.substr(1) == string(m-1, '0'))
		{
			ans++;
			d = string(m-1, '9');
			continue;
		}

		i64 hv = str2i(d.substr(m/2));
		if (hv > 0)
		{
			ans += hv-1;
			FORD(j, m/2, m-2) d[j] = '0';
			d[m-1] = '1';
		}
		else
		{

			int i = m/2;
			while (d.substr(i) == string(m-i, '0'))
				i--;
			ans += pow10(m/2) - 1;
			d[i]--;
			FORD(j, i+1, (m-1)/2) d[j] = '9';
			d[m-1] = '1';
		}

		if ( !(d[0] == '1' && d.substr(1, (m-1)/2) == string((m-1)/2, '0')) )
		{
			string d1 = d;
			reverse(ALL(d));
			if (d1 != d) ans++;
			ans += str2i(d.substr(m/2)) - 1;
		}

		ans += 2;
		d = string(m-1, '9');
	}

	ans += str2i(d);

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

//vi F(1000005, 10000000);
//vi P(1000005, -1);

// void solve_case1(int TN)
// {
// 	int n;
// 	fin >> n;
// 	int ans = F[n];
// 	fout << "Case #" << TN << ": " << ans << endl;
// 	cout << "Case #" << TN << ": " << ans << endl;
// }
// 
// int rev(int n)
// {
// 	int r = 0;
// 	while (n > 0)
// 	{
// 		r = r * 10 + n % 10;
// 		n /= 10;
// 	}
// 	return r;
// }

int main()
{
// 	F[1] = 1;
// 	FORD(i, 1, 999999)
// 	{
// 		if (F[i]+1 < F[i+1])
// 		{
// 			F[i+1] = F[i]+1;
// 			P[i+1] = i;
// 		}
// 		int r = rev(i);
// 		if (F[i]+1 < F[r])
// 		{
// 			F[r] = F[i]+1;
// 			P[r] = i;
// 		}
// 	}

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

#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <queue>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>
#undef max
#undef min

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)
#define FORi(i,n) for (int i = 0; i < (n); ++i)
//template<class C>
//void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }


enum quat { oo, ii, jj, kk, mo, mi, mj, mk };
inline quat next(quat z) { return static_cast<quat>(z+1); };

const quat m[8][8] = {
	{ oo, ii, jj, kk, mo, mi, mj, mk },
	{ ii, mo, kk, mj, mi, oo, mk, jj },
	{ jj, mk, mo, ii, mj, kk, oo, mi },
	{ kk, jj, mi, mo, mk, mj, ii, oo },
	
	{ mo, mi, mj, mk, oo, ii, jj, kk },
	{ mi, oo, mk, jj, ii, mo, kk, mj },
	{ mj, kk, oo, mi, jj, mk, mo, ii },
	{ mk, mj, ii, oo, kk, jj, mi, mo }
};

const quat pw[4][8] = {
	{ oo, oo, oo, oo, oo, oo, oo, oo },
	{ oo, ii, jj, kk, mo, mi, mj, mk },
	{ oo, mo, mo, mo, oo, mo, mo, mo },
	{ oo, mi, mj, mk, mo, ii, jj, kk }
};

vector<quat> convert(const string & s)
{
	vector<quat> res(s.size());
	FOR(i,s.size()) res[i] = static_cast<quat>(s[i] - 'i' + ii);
	return res;
}

vector<quat> repeat(const vector<quat> & v, const long long X)
{
	assert(v.size()*X <= 10000); //small data set
	vector<quat> res;
	FORi(i,X) res.insert(res.end(), v.begin(), v.end());
	return res;
}

const char * solve_case(const string & s, const long long X)
{
	const quat ijk = m[m[ii][jj]][kk]; assert(ijk == mo);
	vector<quat> L = convert(s);
	const size_t n = L.size();
	if (n*X < 3) return "NO";

	quat z = oo;
	FOR(i,n) z = m[z][L[i]];
	if (pw[X%4][z] != ijk) return "NO";
	
	vector<quat> LLL = repeat(L, X);
	size_t a = 0, c = LLL.size(); assert(c == n*X);
	quat La = oo; //prod LLL[0..a)
	quat Lc = oo; //prod LLL[c..end)
	{
		for (; a < c && La != ii; ++a) La = m[La][LLL[a]];
		if (La != ii) return "NO";
		for (; a < c && Lc != kk; --c) Lc = m[LLL[c-1]][Lc];
		if (Lc != kk) return "NO";
		assert(a<c);
		return "YES";

	}
	return "FAIL";
	return "NO";
	return "YES";
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		int L; long long X;
		in >> L >> X; assert(L >= 1);
		string s;
		in >> s; assert(s.size() == L);

		const char * result = solve_case(s, X);
		out << "Case #" << t << ": " << (result) << endl;
	}
}


int main()
{
	//ifstream in("C-sample.in");
	//ofstream out("C-sample-out.txt");

	ifstream in("C-small-attempt0.in");
	ofstream out("C-small-attempt0-out.txt");

	//ifstream in("C-large.in");
	//ofstream out("C-large-out.txt");

	solve(in,out);

	return 0;
}

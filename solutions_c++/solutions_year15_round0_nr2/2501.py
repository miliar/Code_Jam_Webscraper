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
template<class C>
void show(const C & v) { FOR(i,v.size()) cout << v[i] << ' '; cout << endl; }


int solve_case(const priority_queue<int> & d)
{
	int n = d.top();
	int res = n;
	if (n <= 3) return res;
	for (int k = 2; k <= n; ++k) { //k <= n es overkill
		priority_queue<int> dd(d);
		dd.pop();
		for (int i = 0; i < k; ++i) dd.push(n/k + (i < (n%k)));
		int rr = solve_case(dd);
		if (res > rr + k - 1) res = rr + k - 1;
	}
	return res;
}

int solve_case(const vector<int> & P)
{
	const size_t D = P.size();
	show(P);
	//priority_queue<int, vector<int>, less<int> > d(P.begin(), P.end());
	priority_queue<int> d(P.begin(), P.end());
	int res = solve_case(d);
	cout << endl;
	return res;
}

int solve_case_incorrectly(const vector<int> & P)
{
	const size_t D = P.size();
	show(P);
	//priority_queue<int, vector<int>, less<int> > d(P.begin(), P.end());
	priority_queue<int> d(P.begin(), P.end());
	int specials = 0;
	int bk = d.top();
	int res = bk;
	while (bk > 3) {
		int lrg = bk;
		cout << lrg << ' ';
		d.pop();
		d.push(lrg/2);
		d.push(lrg-lrg/2);
		++specials;
		bk = d.top();
		if (bk + specials < res)
			res = bk + specials;
	}
	cout << endl;
	return res;
}

int solve_case_incorrectly2(const vector<int> & P)
{
	const size_t D = P.size();
	show(P);
	multiset<int> d(P.begin(), P.end());
	int specials = 0;
	multiset<int>::iterator bk = --d.end();
	int res = *bk;
	while (*bk > 3) {
		int lrg = *bk;
		cout << lrg << ' ';
		d.erase(bk);
		d.insert(lrg/2);
		d.insert(lrg-lrg/2);
		++specials;
		bk = --d.end();
		if (*bk + specials < res)
			res = *bk + specials;
	}
	cout << endl;
	//int res = *bk + specials;
	return res;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		cout << "Case #" << t << endl;
		int D;
		in >> D; assert(D >= 1);
		vector<int> P(D);
		FOR(i,D) { in >> P[i]; }

		int result = solve_case(P);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//for (int n = 1; n < 100; ++n) {
	//	int m = n;
	//	for (int k = 1; k < n; ++k) {
	//		int mm = (n+k)/(k+1) + k;
	//		if ( m > mm ) m = mm;
	//	}
	//	cout << n << ' ' << m << '\t';
	//}
	//cout << endl;
	//return 0;


	//ifstream in("B-sample2.in");
	//ofstream out("B-sample2-out.txt");

	ifstream in("B-small-attempt2.in");
	ofstream out("B-small-attempt2-out.txt");

	//ifstream in("B-large.in");
	//ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}

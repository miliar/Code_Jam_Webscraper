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



//int validate(const int N, const vector<int> & A)
//{
//	vector<int> b;
//	int res = INT_MAX;
//	FOR(c, (1<<N)) {
//		b = A;
//		int sw = 0;
//		for (int i = 0; i < N; i++) {
//			if (c & (1 << i)) {
//				for (int j = 0; j >)
//			}
//		}
//	}
//}

int solve_case2(const int N, const vector<int> & A)
{
	vector<int> b(A);
	assert(N == b.size());

	int res = 0;
	for (int i0 = 0, i1 = N; i0 < i1; ) {
		int sw = 0;
		auto jj = min_element(b.begin()+i0, b.begin()+i1);
		int j = jj-b.begin();
		assert(i0 <= j && j < i1);
		if (j-i0 <= i1-1-j) {
			while (i0 < j) {
				swap(b[j-1],b[j]);
				++res;
				--j;
			}
			++i0;
		} else {
			while (j+1 < i1) {
				swap(b[j],b[j+1]);
				++res;
				++j;
			}
			--i1;
		}
	}
	//cout << res << ": "; show(b); 
	return res;
}

//int solve_case(const int N, const vector< pair<int,int> > & A)
int solve_case(const int N, const vector<int> & A)
{
	show(A);
	if (N == 1) return 0;
	vector<int> b;

	int res = INT_MAX;
	FORi(i,N) {
		b = A;
		int sw = 0;
		assert(N == b.size());
		for (int j = 0; j < i; ++j)
		{
			for (int k = j; k-1 >= 0; --k)
			{
				if (b[k-1]>b[k]) { swap(b[k-1],b[k]), ++sw; }
			}
		}
		for (int j = i; j < N; ++j)
		{
			for (int k = j; k-1 >= i; --k)
			{
				if (b[k-1]<b[k]) { swap(b[k-1],b[k]), ++sw; }
			}
		}

		if (res > sw) {cout << sw << ": "; show(b); }
		res = min(res, sw);
	}

	if (N == 2) assert(res == 0);
	int res2 = solve_case2(N, A);
	assert(res == res2);
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
		//cout << "Case #" << t << endl;
		int N;
		in >> N; assert(N >= 1);
		//vector< pair<int,int> > A(N);
		//FOR(i,N) { in >> A[i].first; A[i].second = i; }
		vector<int> A(N);
		FOR(i,N) { in >> A[i]; }

		int result = solve_case2(N, A);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("B-sample.in");
	//ofstream out("B-sample-out.txt");

	//ifstream in("B-small-attempt0.in");
	//ifstream in("B-small-attempt2.in");
	//ofstream out("B-small-out.txt");

	ifstream in("B-large.in");
	ofstream out("B-large-out.txt");

	solve(in,out);

	return 0;
}

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
#include <sstream>
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
#define ALL(x) (x).begin(), (x).end()

const int ENGLISH = 1;
const int FRENCH = 2;
const int BOTH = ENGLISH | FRENCH;
inline int other(int l) { return 3 - l; }

int assignlang(const vector<int> & sent, int l, vector<int> & lang)
{
	int bothincreased = 0;
	FOR(i,sent.size()) {
		if (lang[sent[i]] == other(l)) ++bothincreased;
		lang[sent[i]] |= l;
	}
	return bothincreased;
}

int solve_case_recursive(
	const int N, const int n, 
	const vector< vector<int> > & wordsinsentence,
	const vector< vector<int> > & sentenceswithword,
	int i,
	const vector<int> & lang
	)
{
	if (i == N) return 0;
	int botheng = 0, bothfr = 0;
	{
		vector<int> lcopy(lang);
		botheng += assignlang(wordsinsentence[i], ENGLISH, lcopy);
		botheng += solve_case_recursive(N, n, wordsinsentence, sentenceswithword, i+1, lcopy);
	}
	{
		vector<int> lcopy(lang);
		bothfr += assignlang(wordsinsentence[i], FRENCH, lcopy);
		bothfr += solve_case_recursive(N, n, wordsinsentence, sentenceswithword, i+1, lcopy);
	}
	return min(botheng, bothfr);
}

int solve_case(const vector< vector<string> > & ss)
{
	const int N = ss.size();
	map<string, int> m; int n = 1;
	for_each(ALL(ss), [&](const vector<string> & s){
		for_each(ALL(s), [&](const string & w){
			int & idx = m[w];
			if (idx == 0) idx = n++;
		});
	});

	vector< vector<int> > wordsinsentence(N);
	vector< vector<int> > sentenceswithword(n);
	FOR(i, N) {
		for_each(ALL(ss[i]), [&](const string & w){
			int idx = m[w];
			wordsinsentence[i].push_back(idx);
			sentenceswithword[idx].push_back(i);
		});
	};

	vector<int> lang(n, 0);

	assert(N>=2);
	int both = 0;
	both += assignlang(wordsinsentence[0], ENGLISH, lang);
	both += assignlang(wordsinsentence[1], FRENCH, lang);

	int res = both + solve_case_recursive(N, n, wordsinsentence, sentenceswithword, 2, lang);
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
		cout << t << endl;
		int N; 
		in >> N; in >> ws;
		vector< vector<string> > ss(N);
		FOR(i,N) {
			string s;
			getline(in, s);
			istringstream inn(s);
			string w;
			while(inn >> w)	ss[i].push_back(w);
		}

		int result = solve_case(ss);
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

#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>

using namespace std; 

#define BUG(x) if (DEBUG) cout << __LINE__ << ": " << #x << " = " << x << endl; 
#define LET(x, a) __typeof(a) x = a
#define FOREACH(it, v) for(LET(it, (v).begin()); it != (v).end(); ++it) 

typedef long long LL; 

template <class T> inline int size(const T& c) {return (int) c.size();} 
inline LL two(int x) {return (1LL << (x));}
int readInt() {int N = -1; scanf("%d", &N); return N;}
string readString() {char buffer[1 << 20]; scanf("%s", buffer); return buffer;}
template <class T> ostream& operator << (ostream& o, const vector <T>& v) {o << "{"; FOREACH(it, v) o << *it << ","; return o << "}";} 
template <class A, class B> ostream& operator << (ostream& o, const pair <A, B>& p) {o << "("; o << p.first << "," << p.second << ")"; return o;} 

const bool DEBUG = true; 
const double epsilon = 1e-8; 
const int infinite  = 1000000000; 
const LL infiniteLongLong = 1000000000000000000LL; 

struct Solver
{
	vector < vector <int> > v;
	string solve(vector < vector <int> >& v) {
		this -> v = v;
		vector < vector <int> > rows;
		vector < vector <int> > cols;
		for (int i = 0; i < size(v); ++i)
			rows.push_back(v[i]);
		for (int j = 0; j < size(v[0]); ++j) {
			vector <int> col;
			for (int i = 0; i < size(v); ++i) {
				col.push_back(v[i][j]);
			}
			cols.push_back(col);
		}
		for (int i = 0; i < size(rows); ++i)
			sort(rows[i].begin(), rows[i].end());
		for (int j = 0; j < size(cols); ++j)
			sort(cols[j].begin(), cols[j].end());
		int lThisRow = size(rows[0]) - 1;
		int lThisCol = size(cols[0]) - 1;
		for (int i = 0; i < size(v); ++i) {
			for (int j = 0; j < size(v[i]); ++j) {
				int r = i, c = j;
				if (v[i][j] != rows[r][lThisRow] && v[i][j] != cols[c][lThisCol]) {
					return "NO";
				}
			}
		}
		return "YES";
	}
};

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		int M = readInt(), N = readInt();
		vector < vector <int> > v(M, vector <int> (N, 0));
		for (int i = 0; i < M; ++i)
			for (int j = 0; j < N; ++j)
				v[i][j] = readInt();
		Solver solver;
		string result = solver.solve(v);
		printf("Case #%d: %s\n", test, result.c_str());	
	}
	return 0;
}

// Powered by PhoenixAI

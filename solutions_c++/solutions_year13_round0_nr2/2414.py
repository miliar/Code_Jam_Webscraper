/*
LANG: C++
ID: he.andr1
PROG: B
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<cstring>
#include<cassert>
#include<stack>
#include<list>
#include<cstdio>
#include<numeric>
#include<complex>
#include<string>
#include<map>

using namespace std;

#define DEBUG 1

#ifdef DEBUG
	#define ERR cerr
#else
	#define ERR if(true); else cerr
#endif

#define ITER(v, i) for(__typeof(v.begin()) i = v.begin(); i != v.end(); i++) 
#define X real()
#define Y imag()
#define A first
#define B second

typedef pair<int, int> pii;
typedef complex<int> pt;
typedef long long ll;

template <class T> T cross(complex<T> a, complex<T> b) { return imag(a * conj(b)); }

template <class T> T min(T a, T b, T c) { return min(a, min(b, c)); }

template <class T> T max(T a, T b, T c) { return max(a, max(b, c)); }

template <class T> void setmin(T &a, T b) { if(b < a) a = b; }

template <class T> void setmax(T &a, T b) { if(b > a) a = b; }

const int MAXN = 105, MAXM = 105;
const int MAXA = 105;

int N, M;
int A[MAXN][MAXM];
int rMax[MAXN];
int cMax[MAXM];

void io(istream &in, ostream &out) {
	int T; 
	in >> T;
	for(int z = 1; z <= T; z++) {
		in >> N >> M;
		memset(rMax, 0, sizeof(rMax));
		memset(cMax, 0, sizeof(cMax));
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				in >> A[i][j];
				setmax(rMax[i], A[i][j]);
				setmax(cMax[j], A[i][j]);
			}
		}
		bool good = true;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(rMax[i] > A[i][j] && cMax[j] > A[i][j]) good = false;
			}
		}
		out << "Case #" << z << ": ";
		if(good) out << "YES";
		else out << "NO";
		out << '\n';
	}
}

int main() {
	ifstream fin ("B-large.in");
	if(fin.good()) {
		ofstream fout ("B-large.out");
		io(fin, fout);
		fin.close();
		fout.close();
	} else 
		io(cin, cout);
	return 0;
}

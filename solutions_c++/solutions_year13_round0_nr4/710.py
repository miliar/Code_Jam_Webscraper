/*
LANG: C++
ID: he.andr1
PROG: D
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
#include<bitset>
#include<string>

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

const int MAXN = 205;
const int MAXK = 405;
const int MAXV = 205;

typedef vector<bool> bmask;

int N, K0, V[MAXN], K[MAXN];
int keys[MAXV];
vector<int> chests[MAXN];
int C[MAXN];

set<bmask> seen;

bool dfs(int pos, bmask used) {
	if(pos == N) return true;
	if(!(seen.insert(used).B)) return false;
	for(int i = 0; i < N; i++) {
		if(!(used[i]) && keys[V[i]] > 0) {
			C[pos] = i + 1;
			used[i] = true;
			keys[V[i]] --;
			ITER(chests[i], k) {
				keys[*k] ++;
			}
			if(dfs(pos + 1, used)) return true;
			if(keys[V[i]]) return false;
			used[i] = false;
			ITER(chests[i], k) {
				keys[*k] --;
			}
			keys[V[i]] ++;
		}
	}
	return false;
}


void io(istream &in, ostream &out) {
	int T; in >> T;
	for(int z = 1; z <= T; z++) {
		in >> K0 >> N;
		memset(keys, 0, sizeof(keys));
		for(int i = 0; i < K0; i++) {
			int v; in >> v;
			keys[v - 1] ++;
		}
		for(int i = 0; i < N; i++) {
			in >> V[i]; V[i]--;
			in >> K[i];
			chests[i].clear();
			for(int j = 0; j < K[i]; j++) {
				int v;
				in >> v; v--;
				chests[i].push_back(v);
			}
		}
		out << "Case #" << z << ": ";
		seen.clear();
		bmask start(N);
		if(dfs(0, start)) {
			out << C[0];
			for(int i = 1; i < N; i++) {
				out << ' ' << C[i];
			}
		} else {
			out << "IMPOSSIBLE";
		}
		out << '\n';
		ERR << z << '\n';
	}
}

int main() {
	ifstream fin ("D-small-attempt1.in");
	if(fin.good()) {
		ofstream fout ("D-small-attempt1.out");
		io(fin, fout);
		fin.close();
		fout.close();
	} else 
		io(cin, cout);
	return 0;
}

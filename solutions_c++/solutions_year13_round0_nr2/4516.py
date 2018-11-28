#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for (int i(0),_n(n); i < _n; ++i)
#define FOR(i,a,b) for (int i(a),_b(b); i < _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define ALL(x) (x).begin(),(x).end()
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair((a),(b))
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define debug if(1)printf

int TCases;

int grass[100][100];
int N, M;


void read_case() {
	cin >> N >> M;
	FOR(r,0,N) {
		FOR(c,0,M) {
			cin >> grass[r][c];
		}
	}

}

void solve_case() {
	int maxr[100], maxc[100];
	memset(maxr, 0, sizeof(maxr));
	memset(maxc, 0, sizeof(maxc));

	FOR(r,0,N) {
		FOR(c,0,M) {
			maxr[r] = max(maxr[r], grass[r][c]);
			maxc[c] = max(maxc[c], grass[r][c]);
		}
	}

	/*
	cout << N << " " << M << endl;
	FOR(r,0,N) { cout << maxr[r] << "| "; }
	cout << endl;
	FOR(c,0,M) { cout << maxc[c] << "| "; }
	cout << endl;
	*/
	
	
	
	bool possible = true;
	FOR(r,0,N) {
		FOR(c,0,M) {
			if (grass[r][c]<maxr[r] && grass[r][c]<maxc[c]) {
				possible = false;
				break;
			}
		}
		if (!possible) break;
	}
	
	cout << (possible?"YES":"NO") << endl;
	
}

	

int main() {
	cin >> TCases;
	for (int nCase=1; nCase<=TCases; nCase++) {
		read_case();
		cout <<"Case #" << nCase << ": ";
		solve_case();
	}
	return 0;
}
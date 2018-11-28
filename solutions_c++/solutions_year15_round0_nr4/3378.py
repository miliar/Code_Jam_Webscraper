#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>
#include <queue>
#include <stack>
#include <cassert>
#include <cstring>
#include <climits>
#include <functional>
#include <unordered_set>
#include <unordered_map>
#define VAR(i,v) __typeof(v) i = (v)
#define SIZE(x) ((int)(x).size())
#define ALL(x) (x).begin(), (x).end()
#define REP(i,b) for(int i=0; i<(b); ++i)
#define FOR(i,a,b) for(int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for(int i=(a); i>=(b); --i)
#define FOREACH(i,c) for(VAR(i,(c).begin()); i != (c).end(); ++i)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define NL printf("\n")

using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;

const int INF = 2147483640;
const int MAXN = 1000005;

int main() {
	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	REP(i,t) {
		int x, r, c;
		cin >> x >> r >> c;

		bool ans = 0;

		if(x == 1) ans = 1;
		if(x == 2) if(r%2==0 || c%2==0) ans = 1;
		if(x == 3) {
			REP(i,2) {
				if(r==3 && c==2) ans = 1;
				if(r==3 && c==3) ans = 1;
				if(r==4 && c==3) ans = 1;
				if(r==4 && c==4) ans = 1;
				swap(r,c);
			}
		}
		if(x == 4) {
			REP(i,2) {
				if(r==4 && c==3) ans = 1;
				if(r==4 && c==4) ans = 1;
				swap(r,c);
			}

		}

		cout << "Case #" << i+1 << ": " << (ans?"GABRIEL":"RICHARD") << endl;
	}

	return 0;
}

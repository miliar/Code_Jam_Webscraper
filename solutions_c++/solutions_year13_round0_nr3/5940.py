#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp make_pair
#define pb push_back

static inline bool ispal(int x) {
	stringstream s;
	s << x;
	string str = s.str();
	return s.str() == string(str.rbegin(), str.rend());
}
 
int main() {
	int T;
	cin >> T;
	for(int i=0; i!=T; i++) {
		int A, B;
		cin >> A >> B;
		int cnt = 0;
		FOR(j, A, B+1) {
			int x = sqrt(j);
			if(x*x != j)
				continue;
			if(!ispal(x) || !ispal(j))
				continue;
			cnt++;
		}
		cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	return 0;
}

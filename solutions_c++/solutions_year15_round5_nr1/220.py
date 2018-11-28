#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <unordered_map>
#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second

const int MAX = 1000*1100;
int n, d;
VI kids[MAX];

int salary[MAX];
pii range[MAX];

void DFS(int v, int min_sal, int max_sal){
	min_sal = min(min_sal, salary[v]);
	max_sal = max(max_sal, salary[v]);
	//cerr << v << ' ' << min_sal << ' ' << max_sal << endl;
	range[v] = pii(min_sal, max_sal);

	foreach(kids[v], it)
		DFS(*it, min_sal, max_sal);
}

int add[2*MAX];
int rem[2*MAX];

int main(){
	ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	FOR(cnt,0,tests){
		cin >> n >> d;
		FOR(i,0,n){
			kids[i].clear();
		}
		LL s0, as, cs, rs;
		LL m0, am, cm, rm;
		cin >> s0 >> as >> cs >> rs >> m0 >> am >> cm >> rm;
		salary[0] = s0;
		FOR(i,1,n){
			s0 = (as*s0+cs)%rs;
			m0 = (am*m0+cm)%rm;
			salary[i] = s0;
			kids[(int)m0%i].push_back(i);
		}

		DFS(0, salary[0], salary[0]);
		fill(add, add+2*MAX, 0);
		fill(rem, rem+2*MAX, 0);
		FOR(i,0,n) if(range[i].SC-range[i].FR <= d){
			add[max(0, range[i].SC-d)]++;
			rem[range[i].FR+1]++;
		}

		int ans = 0, cur = 0;
		FOR(i,0,2*MAX){
			cur += add[i]-rem[i];
			ans = max(ans, cur);
		}
		cout << "Case #" << cnt+1 << ": " << ans << '\n';

	}

	return 0;
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cctype>
#define SZ(x) ( (int) (x).size() )
#define me(x,a) memset(x,a,sizeof(x))
#define FN(a,n) for(int a=0;a<n;a++)
#define FOR(a,ini,fin) for(int a=(ini);a<(fin);a++)
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d %d",&x,&y)
#define sc3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define all(v) v.begin(),v.end()
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define endl "\n"
#define MOD 1000000007
#define MAXN 1000006
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
using namespace std;

int f[1003], cyr[1003];
vector<int> rev[1003];
int v[1003];
int cnt, cc;
stack<int> st;
bool istwo ;
int deep;
void dfs2(int x, int d) {
	deep = max(deep, d);
	FN (i, SZ(rev[x])) {
		int son = rev[x][i];
		dfs2(son, d + 1);
	}
}

void dfs(int x) {
	v[x] = cc;
	st.push(x);
	if (v[f[x]] == -1) dfs(f[x]);
	else if (v[f[x]] == cc) {
		// cnt
		cnt = 0;	
		int node;
		vector<int> cy;
		do {
			// components of the cycle
			node = st.top();
			cy.pb(node);
			st.pop();
			cnt++;
		} while (node != f[x]);
		
		cyr[cy[SZ(cy) - 1]] = cy[0];
		FOR (k, 1, SZ(cy)) {
			cyr[cy[k - 1]] = cy[k];
		}
		
		// getting two best outs
		vector<int> deeps;
		FN (k, SZ(cy)) {
			int node = cy[k];
			int maxdeep = 0;
			FN (j, SZ(rev[node])) {
				int son = rev[node][j];
				if (son != cyr[node]) {
					deep = 0;
					dfs2(son, 1);
					maxdeep = max(maxdeep, deep);
				}
			}
			deeps.pb(maxdeep);
		}
		deeps.pb(0);
		deeps.pb(0);
		sort(deeps.begin(), deeps.end());
		if (SZ(cy) == 2) {
			istwo = true;
			cnt += deeps[SZ(deeps) - 1];
			cnt += deeps[SZ(deeps) - 2];
		}
	}
	if (!st.empty()) st.pop();
}

int main() {
	int tc;
	sc1(tc);
	FN (itc, tc) {
		int n;
		sc1(n);
		me(v, -1);
		
		FN (i, n) rev[i].clear();
		
		FN (i, n) {
			sc1(f[i]);
			f[i]--;
			rev[f[i]].pb(i);
		}
		int maxi = 0;
		int sumtwo = 0;
		cc = 0;
		FN (i, n) {
			if (v[i] == -1) {
				cnt = 0;	
				istwo = 0;
				while (!st.empty()) st.pop();
				dfs(i);
				if (istwo) sumtwo += cnt;
				else maxi = max(maxi, cnt);
				cc++;
			}
		}
		maxi = max(maxi, sumtwo);
		
		printf("Case #%d: %d\n", (itc + 1), maxi);
	}
}

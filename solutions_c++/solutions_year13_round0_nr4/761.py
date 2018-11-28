#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

int have[333][333];
vector<int> edge[333];
vector<int> keys[333];
int need[333];
bool ban[333];

vector<int> dirEdge[333];

int k, n;

int dfn[333];
int low[333];
bool instack[333];
int stack[333];
int now[333];

int balance[333];
int sign, NP, top;

void dfs(int v)
{
	dfn[v] = low[v] = ++sign;
	instack[v] = true;
	stack[++top] = v;
	for (int i=0;i<edge[v].size();i++)
	{
		int u = edge[v][i];
		if (!dfn[u])
		{
			dfs(u);
			low[v] = min(low[v], low[u]);
		}else
		if (instack[u])
			low[v] = min(low[v], low[u]);
	}
	if (dfn[v] == low[v])
	{
		NP++;
		do
		{
			instack[stack[top]] = false;
			now[stack[top]] = NP;
			top--;
		}while (stack[top+1] != v);
	}
}

void SCC()
{
	NP = top = sign = 0;
	// memset(dfn,0,sizeof(dfn));
	// memset(instack,0,sizeof(instack));
	// memset(stack,0,sizeof(stack));
	REP(i, n + 1) dfn[i] = instack[i] = stack[i] = 0;
	for (int i=0;i<=n;i++)
	if (!dfn[i] && !ban[i])
		dfs(i);
}

void surf(int x) {
	dfn[x] = 1;
	TR(it, dirEdge[x]) {
		if (!dfn[*it]) {
			surf(*it);
		}
	}
}

bool go() {
	REP(i, n + 1) edge[i].clear();
	REP(i, n + 1) {
		if (ban[i]) continue;
		REP(j, n + 1) {
			if (!j || ban[j]) continue;
			if (have[i][need[j]]) {
				edge[i].PB(j);
			}
		}
	}

	SCC();
	// cout << "NP = " << NP << endl;
	REP(i, n + 1) if (!ban[i]) --now[i];
	REP(i, NP) dirEdge[i].clear();
	// REP(i, n + 1) cout << "now[i] = " << now[i] << endl;
	REP(i, n + 1) {
		if (ban[i]) continue;
		TR(it, edge[i]) {
			if (now[i] == now[*it]) {
				continue;
			}

			dirEdge[now[i]].PB(now[*it]);
			//cout << "i = " << now[i] << " *it = " << now[*it] << endl;
		}
	}

	REP(i, NP) dfn[i] = 0;
	surf(now[0]);
	REP(i, NP) if (!dfn[i]) return false;

	return true;
}

void solve(int caseId) {
	vector<int> diffKeys;
	cin >> k >> n;
	REP(i, n + 1) keys[i].clear();
	keys[0].resize(k);
	REP(i, k) scanf("%d", &keys[0][i]);
	for (int i = 1; i <= n; ++i) {
		scanf("%d%d", &need[i], &k);
		keys[i].resize(k);
		REP(j, k) scanf("%d", &keys[i][j]);
		diffKeys.PB(need[i]);
	}

	REP(i, n + 1) REP(j, keys[i].size()) diffKeys.PB(keys[i][j]);
	SORT(diffKeys);
	diffKeys.erase(unique(ALL(diffKeys)), diffKeys.end());
	REP(i, n + 1) REP(j, keys[i].size()) keys[i][j] = lower_bound(ALL(diffKeys), keys[i][j]) - diffKeys.begin();
	for (int i = 1; i <= n; ++i) {
		need[i] = lower_bound(ALL(diffKeys), need[i]) - diffKeys.begin();
	}

	REP(i, n + 1) REP(j, diffKeys.size()) have[i][j] = 0;
	REP(i, n + 1) REP(j, keys[i].size()) ++have[i][keys[i][j]];

	REP(i, diffKeys.size()) balance[i] = 0;
	REP(i, n + 1) TR(it, keys[i]) ++balance[*it];
	REP(i, n) --balance[need[i + 1]];
	bool bad = false;
	REP(i, n + 1) ban[i] = false;
	REP(i, diffKeys.size()) if (balance[i] < 0) bad = true;
	//cout << "bad = " << bad << endl;
	if (!bad) if (!go()) bad = true;
	cout << "Case #" << caseId << ":";
	if (bad) {
		cout << " IMPOSSIBLE" << endl;
		return;
	}

	REP(iter, n) {

		for (int i = 1; i <= n; ++i) {
			if (!ban[i] && have[0][need[i]]) {
				--have[0][need[i]];
				TR(it, keys[i]) {
					++have[0][*it];
				}
				ban[i] = true;
				if (!go()) {
					ban[i] = false;
					++have[0][need[i]];
					TR(it, keys[i]) {
						--have[0][*it];
					}

					continue;
				}

				cout << " " << i;
				break;
			}
		}
	}

	cout << endl;

}

int main() {
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; ++testCase) {
		solve(testCase);
	}
	return 0;
}
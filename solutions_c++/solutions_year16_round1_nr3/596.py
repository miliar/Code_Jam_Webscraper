#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

vector<vector<int> > cycles;
bool done[2000], visited[2000];
bool dump;
int twice;
vector<int> g;

void findCycle(int v) {
	if (done[v])
		return;
	visited[v] = true;
	int next = g[v];
	if (visited[next]) {
		dump = true;
		twice = next;
		vector<int> em;
		cycles.pb(em);
	}
	else
		findCycle(next);
	if (dump) {
		cycles[cycles.sz - 1].pb(v);
		done[v] = true;
		if (v == twice)
			dump = false;
	}
}

int longest(int v) {
	if (visited[v])
		return 0;
	int ret = 0;
	FOR (i, g.sz)
		if (g[i] == v)
			ret = max(ret, longest(i));
	return ret + 1;
}

int main() {
  freopen("Cl.out","wt", stdout);
  freopen("Cl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int n;
    cin >> n;
    g.clear();
    FOR (i, n) {
    	int a;
    	cin >> a;
    	g.pb(a - 1);
    }
    cycles.clear();
    SET(done, 0);
    FOR (i, n) {
    	if (!done[i]) {
    		dump = false;
    		twice = -1;
    		SET(visited, 0);
    		findCycle(i);
    	}
    }
    
    int ret = 0;
    FOR (i, cycles.sz)
    	ret = max((signed int)cycles[i].sz, ret);
    int sum = 0;
    FOR (i, cycles.sz) {
    	if (cycles[i].sz == 2) {
    		int a = cycles[i][0], b = cycles[i][1];
    		SET(visited, 0);
    		visited[b] = true;
    		sum += longest(a);
    		SET(visited, 0);
    		visited[a] = true;
    		sum += longest(b);
    	}
    }
    ret = max(ret, sum);
    cout << ret;
    cout << "\n";
  }
  return 0;
}

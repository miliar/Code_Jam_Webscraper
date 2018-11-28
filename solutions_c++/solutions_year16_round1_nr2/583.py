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

vector<vector<int> > lists, sorted[100];

bool used[200];

int main() {
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int n;
    cin >> n;
    lists.clear();
    FOR (i, 2 * n - 1) {
    	vector<int> a;
    	int b;
    	FOR (j, n) {
    		cin >> b;
    		a.pb(b);
    	}
    	lists.pb(a);
    }
    FOR (i, n)
    	sorted[i].clear();
    SET(used, 0);
    FOR (i, n) {
    	int mm = 1 << 20;
    	FOR (j, lists.sz)
    		if (!used[j])
    			mm = min(mm, lists[j][i]);
    	FOR (j, lists.sz) {
    		if (used[j])
    			continue;
    		if (lists[j][i] == mm) {
    			used[j] = true;
    			sorted[i].pb(lists[j]);
    		}
    	}
    }
    int missing = -1;
    FOR (i, n)
    	if (sorted[i].sz == 1)
    		missing = i;
    FOR (i, n) {
    	if (i)
    		cout << " ";
    	int curr = sorted[missing][0][i];
    	if (missing == i)
    		cout << curr;
    	else {
    		if (sorted[i][0][missing] == curr)
    			cout << sorted[i][1][missing];
    		else
    			cout << sorted[i][0][missing];
    	}
    }
    cout << "\n";
  }
  return 0;
}

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

const double pi = acos(-1.0);
const int size = 1000 * 1000 + 100;

set <int> vertex[size];
bool inans[size];
int cur;
vector <pair <long long, int> > salary;
int n;
long long d, as, cs, rs;
long long am, cm, rm;
int tc;

long long s[size], m[size];

int dfs(int v, bool state) {
	inans[v] = state;
	int cnt = 1;
	for (set <int>::iterator it = vertex[v].begin(); it != vertex[v].end(); ++it) {
		cnt += dfs(*it, state);  
	}

	return cnt;
}

void turnon(int v) {
	if (v > 0)
		vertex[m[v]].insert(v);
		
	if (v == 0 || inans[m[v]]) {
		cur += dfs(v, true);	
	}
}

void turnof(int v) {
	if (v > 0)
		vertex[m[v]].erase(v);
		
	if (inans[v]) {
		cur -= dfs(v, false);
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> tc;
    for (int tnum = 0; tnum < tc; tnum++) {
    	cin >> n >> d;
		for (int i = 0; i < n; i++) {
			vertex[i].clear();
			inans[i] = false;
		}
    	salary.clear();

        cin >> s[0] >> as >> cs >> rs;
        cin >> m[0] >> am >> cm >> rm;

		int ans = 1;
		cur = 0;

	  	for (int i = 1; i < n; i++) {
	  		s[i] = (s[i - 1] * as + cs) % rs;
	  		m[i] = (m[i - 1] * am + cm) % rm;
	  	}
	  	for (int i = 1; i < n; i++)
	  		m[i] %= i;
	  	for (int i = 0; i < n; i++) {
	  		salary.pb(mp(s[i], i));
	//  		cerr << i << ' ' << m[i] << ' ' << s[i] << endl;
	  	}
	  	sort(salary.begin(), salary.end());

	  	int p = 0;
	  	for (int i = 0; i < n; i++) {
	  		while (p < n && salary[p].fs <= salary[i].fs + d) {
	  			turnon(salary[p].sc);
	  			p++;
	  		}
	  		ans = max(ans, cur);
	  		turnof(salary[i].sc);
	  	}

	  	cerr << tnum + 1 << endl;
	  	cout << "Case #" << tnum + 1 << ": " << ans << endl;
    }

    return 0;
}
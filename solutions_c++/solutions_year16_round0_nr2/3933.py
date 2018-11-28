#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#ifndef ONLINE_JUDGE
	#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#else
	#define DEBUG(x) do {} while(0);
#endif

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
typedef long long ll;
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

int n,m;
int T;
char istr[111];

void solve() {
	scanf("%s", istr);
	n = strlen(istr);
	queue< pair<int, string> > S;
	S.push(make_pair(0, string(istr)));
	string win;
	set<string> vis;
	REP(i, n) win += "+";
	while(!S.empty()) {
		auto curr = S.front();
		S.pop();
		if(curr.second == win) {
			printf("%d", curr.first);
			break;
		}
	
		for(int idx = 0; idx < n; idx++) {
			string nstr = curr.second;
			reverse(nstr.begin(), nstr.begin()+idx+1);
			for(int j = 0; j <= idx; j++)
				nstr[j] = nstr[j] == '-' ? '+' : '-';
			//printf("curr is %s, nstr: %s\n", curr.second.c_str(), nstr.c_str());
			if(vis.find(nstr) == vis.end()) {
				S.push(mp(curr.first+1, nstr));
				vis.insert(nstr);
			}
		}
	}
}

int main() {
	scanf("%d", &T);
	REP(testc, T) {
		printf("Case #%d: ", testc+1);
		solve();
		printf("\n");
	}
	return 0;
}

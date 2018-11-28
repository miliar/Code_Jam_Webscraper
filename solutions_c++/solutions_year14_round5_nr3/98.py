#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double R;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

const int U = 0;
const int I = 1;
const int O = 2;
const int MAXX = 2123;

pair<int, int> q[MAXX];
vector<int> out;
int s[MAXX];
int n;
int ans;
int cur;

void dfs(int i){
	if(i == n){
		ans = min(ans, cur);
		return;
	}
	int j;
	if(q[i].se != 0){
		for(j = 0; j < i; j++)
			if(s[j] == q[i].se)
				break;
		if(j < i){
			if(q[i].fi == q[j].fi)
				return;
			s[j] = -1;
			s[i] = q[i].se;
			dfs(i+1);
			s[j] = q[i].se;
			return;
		}

		s[i] = q[i].se;
		if(q[i].fi == O)
			cur++;
		dfs(i+1);
		if(q[i].fi == O)
			cur--;

		for(j = 0; j < i; j++){
			if(q[i].fi != q[j].fi && s[j] == 0){
				s[j] = -1;
				dfs(i+1);
				s[j] = 0;
			}
		}
	}

	else{
		s[i] = 0;
		if(q[i].fi == O)
			cur++;
		dfs(i+1);
		if(q[i].fi == O)
			cur--;

		for(j = 0; j < i; j++){
			if(q[i].fi != q[j].fi && s[j] != -1){
				s[i] = s[j];
				s[j] = -1;
				dfs(i+1);
				s[j] = s[i];
			}
		}
	}
}

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
#endif
	int i0 = 1;
	int T;
	scanf("%d", &T);
	for (i0 = 1; i0 <= T; i0++) {
		int i, j, k;

		scanf("%d", &n);
		for(i = 0; i < n; i++){
			char _s[2];
			scanf("%1s%d", _s, &q[i].se);
			q[i].fi = _s[0]=='E' ? I : O;
		}

		ans = 1<<20;
		cur = 0;
		dfs(0);
		if(ans > n){
			printf("Case #%d: CRIME TIME\n", i0);
			continue;
		}

		for(i = 0; i < n; i++)
			if(q[i].fi == O)
				ans--;
			else
				ans++;

		printf("Case #%d: %d\n", i0, ans);
	}
	return 0;
}

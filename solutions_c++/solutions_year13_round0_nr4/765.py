#include<stdio.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<string.h>
using namespace std;
struct Node {
	int t, k;
	int kr[41];
};
vector<int> ans;
vector<struct Node> d;
int my_key[50];
int dp[1<<20];
int k, n;
struct Node make_node(int t, int k) {
	struct Node tmp;
	tmp.t = t;
	tmp.k = k;
	return tmp;
}

bool dfs(int *my_key, int sta) {
	if (sta == (1 << n) - 1)
		return true;
	if(dp[sta]!=-1){
		return dp[sta];
	}
	for (int i = 0; i < n; i++) {
		if ((sta & (1 <<i )) == 0) {
			if (my_key[d[i].t]) {
				my_key[d[i].t]--;
				ans.push_back(i + 1);
				for (int j = 0; j < d[i].k; j++) {
					my_key[d[i].kr[j]]++;
				}
				if (dfs(my_key, sta | (1 << i)))
					return true;

				for (int j = 0; j < d[i].k; j++) {
					my_key[d[i].kr[j]]--;
				}
				ans.pop_back();
				my_key[d[i].t]++;
			}

		}
	}
	dp[sta]=0;
	return false;
}
int main() {
	freopen("D-small-attempt1.in","r",stdin);
	freopen("o.out","w",stdout);
	int T, cas = 1;
	scanf(" %d", &T);
	while (T--) {

		scanf(" %d %d", &k, &n);
		memset(my_key, 0, sizeof(my_key));
		for(int i=0;i<k;i++){
			int x;
			scanf(" %d",&x);
			my_key[x] ++;
		}
		memset(dp,-1,sizeof(dp));
		ans.clear();
		d.clear();
		for (int i = 0; i < n; i++) {
			int ti, ki;
			scanf(" %d %d", &ti, &ki);
			struct Node tmp;
			tmp.t = ti;
			tmp.k = ki;
			for (int j = 0; j < ki; j++) {
				scanf(" %d", &tmp.kr[j]);
			}
			d.push_back(tmp);
		}
		if (dfs(my_key, 0)) {
			printf("Case #%d:", cas++);
			for (size_t i = 0; i < ans.size(); i++) {
				printf(" %d", ans[i]);
			}
			puts("");
		} else {
			printf("Case #%d: IMPOSSIBLE\n", cas++);
		}
		//fflush(stdout);
	}
	return 0;
}

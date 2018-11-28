#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <vector>
#define MAX 1234234

using namespace std;

int N, K;
int nk[MAX][22];
int dp[MAX];
int path[MAX];
vector <int> keys[23];
int t[25];

int f(int mask){
	if(mask == (1<<N)-1){
		dp[mask] = 1;
		return 1;
	}
	if(dp[mask] != -1)
		return dp[mask];
	int &r = dp[mask];
	r = 0;
	for(int i = 0; r==0 && i < N; i++)
		if((mask & (1<<i)) == 0 && nk[mask][t[i]] > 0){
			r = f(mask | (1<<i));
			if(r)
				path[mask] = i;
		}
	return r;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++){

		int rev[210];
		for (int i = 0; i < 210; i++)
			rev[i] = -1;
		for (int i = 0; i < MAX; i++)
			dp[i] = path[i] = -1;

		scanf("%d%d", &K, &N);
		int ik[25];
		for (int i = 0; i < K; i++)
			scanf("%d", &ik[i]);

		set<int> s;
		s.clear();
		for (int i = 0; i < N; i++){
			int n;
			scanf("%d%d", &t[i], &n);
			s.insert(t[i]);
			keys[i].clear();
			for (int j = 0; j < n; j++){
				int x;
				scanf("%d", &x);
				keys[i].push_back(x);
			}
		}

		set<int>::iterator it = s.begin();
		for(int i = 0; it != s.end(); it++, i++){
			rev[*it] = i;
		}
		for(int i = 0; i < K; i++)
			ik[i] = rev[ik[i]];

		for(int i = 0; i < N; i++){
			for (int j = 0; j < (int)keys[i].size(); j++)
				keys[i][j] = rev[keys[i][j]];
			t[i] = rev[t[i]];
		}

		for(int i = 0; i < (1<<N); i++){
			for (int j = 0; j < 22; j++)
				nk[i][j] = 0;

			for (int l = 0; l < K; l++)
				if(ik[l] != -1)
					nk[i][ik[l]]++;
			for (int j = 0; j < N; j++)
				if(i & (1<<j)){
					nk[i][t[j]]--;
					for (int l = 0; l < (int)keys[j].size(); l++)
						if(keys[j][l] != -1)
							nk[i][keys[j][l]]++;
				}
		}
		f(0);
		printf("Case #%d: ", test);
		if(dp[0]){
			int po = path[0];
			int mask = 0;
			while(po != -1){
				printf("%d ", po+1);
				mask = (mask|(1<<po));
				po = path[mask];
			}
			printf("\n");
		}
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}

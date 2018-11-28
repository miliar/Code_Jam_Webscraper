#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>

using namespace std;

char str[10][20];
int len[10];
vector<int> e[5];
int m;
int check() {
	for (int i = 0; i < m; i++) {
		if (e[i].empty())
			return 0;
	}
	for(int i=m;i<4;i++)
		if(!e[i].empty()) return 0;
	return 1;
}

int solve(int i,int j){
	int ans=0;
	for(int k=0;k<min(len[i],len[j]);k++){
		if(str[i][k]==str[j][k])
			ans++;
		else break;
	}
	return ans;
}
int d[10][10];
int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T, n, ri = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n,&m);
		for (int i = 0; i < n; i++) {
			scanf("%s", str[i]);
			len[i]=strlen(str[i]);
		}
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				d[i][j]=solve(i,j);
		int ans=0,cnt=0;
		for (int i = 0; i < 1<<(2 * n); i++) {
			for (int j = 0; j < 4; j++)
				e[j].clear();
			for (int j = 0; j < n; j++) {
				int t = (i >> (j * 2) & 3);
				e[t].push_back(j);
			}
			if (!check())
				continue;

			int sum=m;
			for (int j = 0; j < m; j++) {
				for (int k = 0; k < e[j].size(); k++) {
					int Max=0;
					for(int p=0;p<k;p++){
						Max=max(Max,d[e[j][k]][e[j][p]]);
					}
					//if(Max==0) printf("%s\n",str[e[j][k]]);
					sum+=len[e[j][k]]-Max;
				}
			}

			if(ans<sum){
				ans=sum,cnt=1;
			}else if(ans==sum) cnt++;

		}
		printf("Case #%d: %d %d\n", ri++, ans,cnt);
	}
	return 0;
}


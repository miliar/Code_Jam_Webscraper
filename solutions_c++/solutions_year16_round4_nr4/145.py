#include <bits/stdc++.h>
using namespace std;

int N,ans,res,Test;
bool ok;
bool useda[5],usedb[5];
bool a[5][5];
char s[5][5];

void dfs(int step){
	if (step>N)return;
	for (int i=0;i<N;i++)
		if (!useda[i]){
			bool found=0;
			for (int j=0;j<N;j++)
				if (!usedb[j]&&a[i][j]){
					found=1;
					useda[i]=usedb[j]=1;
					dfs(step+1);
					if (!ok)return;
					useda[i]=usedb[j]=0;
				}
			if (!found){ok=0;return;}
		}
}

bool check(int up){
	for (int i=0;i<N;i++)
		for (int j=0;j<N;j++){
			a[i][j]=(s[i][j]=='1');
			if (a[i][j]==1&&((up>>(i*N+j))&1)==1)return 0;
			if (((up>>(i*N+j))&1)==1)
				a[i][j]=1;
		}
	ok=1;
	memset(useda,0,sizeof(useda));
	memset(usedb,0,sizeof(usedb));
	dfs(1);
	return ok;
}
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		scanf("%d",&N);
		for (int i=0;i<N;i++)scanf("%s",s[i]);
		int up=1<<(N*N);
		ans=2e9;
		for (int i=0;i<up;i++)
			if (check(i)){
				res=0;
				for (int j=0;j<N*N;j++)
					res+=(i>>j)&1;
				ans=min(ans,res);
			}
		printf("Case #%d: %d\n",tt,ans);
	}
}
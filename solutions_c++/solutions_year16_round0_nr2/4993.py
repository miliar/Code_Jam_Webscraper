#include <bits/stdc++.h>
#define maxn 1009
using namespace std;
int dp[maxn][2],n;
char s[maxn];
int dfs(int x,int c){
	int &ans=dp[x][c];
	if(ans!=-1) return ans;
	if(x==0)
		return ans=0;
	if(c==0){
		if(s[x]=='+')
			return ans=dfs(x-1,c);
		else
			return ans=dfs(x-1,c^1)+1;
	}
	else{
		if(s[x]=='-')
			return ans=dfs(x-1,c);
		else
			return ans=dfs(x-1,c^1)+1;
	}
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int tt,cot=1;
	scanf("%d",&tt);
	while(tt--){
		scanf("%s",s+1);
		n=strlen(s+1);
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",cot++,dfs(n,0));
	}
	//system("pause");
	return 0;
}
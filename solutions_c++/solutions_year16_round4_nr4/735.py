#include <bits/stdc++.h>
using namespace std;
int a[5][5];
int f[5][5];
int p[5];
int b[5];
int n;
int check(int x){
	memset(f,0,sizeof f);
	for (int i=0;i<x;i++)
		for (int j=0;j<n;j++)
			for (int k=0;k<n;k++){
				if ((p[i]&(1<<j))&&(b[i]&(1<<k)))
					f[j][k]=1;
			}
	int tmp=0;
		for (int j=0;j<n;j++)
			for (int k=0;k<n;k++)
			{
				tmp+=f[k][j]^a[k][j];
				if (f[k][j]==0&&1==a[k][j]) return n*n;
			}
	return tmp;
}
int ans;
void dfs(int st1,int st2,int num,int la){
	if (!st1) {
		ans=min(ans,check(num));
		// for (int i=0;i<num;i++)
		// 	printf("%d ", p[i]);
		// puts("");
		// for (int i=0;i<num;i++)
		// 	printf("%d ", b[i]);
		// puts("~");
		return ;
	}
	for (int i=1;i<la;i++)
		for (int j=1;j<=st2;j++){
		int cnt=0;
		for (int k=0;k<n;k++)
			if ((1<<k)&i) cnt++;
		for (int k=0;k<n;k++)
			if ((1<<k)&j) cnt--;
		if (cnt) continue;
		p[num]=i;
		b[num]=j;
		if ((st1&i)==i&&(st2&j)==j) dfs(st1-i,st2-j,num+1,i);
	}
}
int main(){
	freopen("d.txt","r",stdin);
	freopen("ddout.txt","w",stdout); 
	int T,ca=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		getchar();
		char c;
		for (int i=0;i<n;i++){
			for (int j=0;j<n;j++)
			{
				c=getchar();
				a[i][j]=c-'0';
			}
			getchar();
		}
		ans=n*n;
		dfs((1<<n)-1,(1<<n)-1,0,(1<<n));
		printf("Case #%d: %d\n", ++ca,ans);
	}
	return 0;
}
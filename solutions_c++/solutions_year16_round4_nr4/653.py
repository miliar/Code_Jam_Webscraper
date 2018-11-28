#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<string.h>
#include<time.h>
typedef long long lnt;
const lnt mod=1e9+7;
char a[11];
int x[11],ch[11],n,ord[11],in,use[11],ans;

void DFS(int now){
	int k;
	if(now==n+1) return;
	int c=0,pp=ord[now];
	for(k=1;k<=n;k++){
		if(use[k]) continue;
		if((ch[pp]&(1<<(k-1)))==0) continue;
		c=1;
		use[k]=1;
		DFS(now+1);
		use[k]=0;
		
	}
	if(c==0) in=0;
	return;
}
void dfs(int now){
	int k,c,t;
	if(now==n+1){
		//printf("%d %d\n",ch[1],ch[2]);
		for(k=1;k<=n;k++) ord[k]=k;
		do{
			memset(use,0,sizeof(use));
			in=1;
			DFS(1);
			if(in==0) return;
		}while(std::next_permutation(ord+1,ord+n+1)); 
		//compute
		t=0;
		for(k=1;k<=n;k++){
			c=x[k]^ch[k];
			while(c){
				if(c%2==1) t++;
				c/=2;
			}
		}
		if(t<ans) ans=t;
		return;
	}
	for(k=1;k<(1<<n);k++){
		if((k&x[now])!=x[now]) continue;
		ch[now]=k;
		dfs(now+1);
	}
	return;
}
int main(){
	freopen("pD.in","r",stdin);
	freopen("pD.txt","w",stdout);
	int T,k,i,t=0;
	scanf("%d",&T);
	while(T--){
		t++;
		scanf("%d",&n);
		for(k=1;k<=n;k++){
			scanf("%s",a);
			x[k]=0;
			for(i=0;i<n;i++){
				x[k]*=2;
				if(a[i]=='1'){
					x[k]++;
				}
			}
		}
		ans=1e9;
		dfs(1);
		printf("Case #%d: ",t);
		printf("%d\n",ans);
	}
}

#include<stdio.h>
#include<string.h>
#define MAX 105

int map[MAX][MAX];
int law[MAX][MAX];
int hc[MAX],hr[MAX];
int n,m;
int ans;

void solve(){
	int i,j;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
			if(hr[i]<law[i][j])law[i][j]=hr[i];
	for(i=0;i<m;i++)
		for(j=0;j<n;j++)
			if(hc[i]<law[j][i])law[j][i]=hc[i];
		
	ans=1;
	for(i=0;i<n;i++){
		for(j=0;j<m;j++)
			if(map[i][j]!=law[i][j]){
				ans=0;
				break;
			}
		if(ans==0)break;
	}
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,ti=1;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&m);
		int i,j;
		memset(hc,0,sizeof(hc));
		memset(hr,0,sizeof(hr));
		for(i=0;i<n;i++)
			for(j=0;j<m;j++){
				scanf("%d",&map[i][j]);
				if(map[i][j]>hr[i])hr[i]=map[i][j];
				if(map[i][j]>hc[j])hc[j]=map[i][j];
				law[i][j]=100;
			}
		solve();
		printf("Case #%d: ",ti++);
		switch(ans){
			case 0:printf("NO\n");break;
			case 1:printf("YES\n");break;
			default:break;
		}
	}
	return 0;
}
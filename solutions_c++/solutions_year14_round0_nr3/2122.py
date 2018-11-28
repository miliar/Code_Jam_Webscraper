#include<stdio.h>
#include<string.h>
int n,m,c;
int flag;
int a[5];
int ans[10][10];
void dfs(int r,int mx,int left){
	int i,j;
	if (left<0) return;
	if (left==0){
		flag=1;
		for (i=0;i<r;i++){
			for (j=0;j<a[i];j++) ans[i][j]='.';
		}
		return;
	}
	if (r>=n) return;
	for (i=2;i<=mx;i++){
		if (r==0){
			a[r]=i;
			a[r+1]=i;
			dfs(r+2,i,left-2*i);
			if (flag) return;
		}else{
			a[r]=i;
			dfs(r+1,i,left-i);
			if (flag) return;
		}
	}
}
int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int ca,cc;
	int i,j;
	scanf("%d",&ca);
	for (cc=1;cc<=ca;cc++){
		scanf("%d%d%d",&n,&m,&c);
		printf("Case #%d:\n",cc);
		c=n*m-c;
		for (i=0;i<n;i++){
			for (j=0;j<m;j++) ans[i][j]='*';
		}
		if (c==1){

		}else if (n==1){
			if (c<2){
				printf("Impossible\n");
				continue;
			}else{
				for (int i=0;i<c;i++) ans[0][i]='.';
			}
		}else if (m==1){
			if (c<2){
				printf("Impossible\n");
				continue;
			}else{
				for (int i=0;i<c;i++) ans[i][0]='.';
			}
		}else{
			flag=0;
			dfs(0,m,c);
			if (!flag){
				printf("Impossible\n");
				continue;
			}
		}
		ans[0][0]='c';
		for (i=0;i<n;i++){
			for (j=0;j<m;j++) printf("%c",ans[i][j]);
			printf("\n");
		}

	}
	return 0;
}

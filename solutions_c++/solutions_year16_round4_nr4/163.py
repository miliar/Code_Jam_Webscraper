#include<stdio.h>
bool f[9][9];
int n,res;
int arrived, ordered;
bool c(int id){
	if(arrived == (1<<n)-1)return true;
	for(int j=0; j<n; j++)
		if((arrived&(1<<j)) == 0){
			//suppose user j arrived
			bool flag = true;
			for(int k=0; k<n; k++)
				if(f[j][k] && (ordered&(1<<k))==0){
					//suppose user j operate k
					flag = false;
					ordered |= 1<<k;
					arrived |= 1<<j;
					if(!c(id+1))return false;
					ordered -= 1<<k;
					arrived -= 1<<j;
				}
			if(flag)return false;
		}
	return true;
}
bool chk(){
	arrived = 0;
	ordered = 0;
	return c(0);
}
void dfs(int i,int j,int tot){
	if(tot >= res)return;
	if(i==n){
		if(chk()){
			if(res > tot)
				res = tot;
		}
		return;
	}
	if(j==n){
		dfs(i+1,0,tot);
		return;
	}
	if(f[i][j]){
		dfs(i,j+1,tot);
		return;
	}
	dfs(i,j+1,tot);
	f[i][j]=true;
	dfs(i,j+1,tot+1);
	f[i][j]=false;
}
int main(){
	int _;char s[9];
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		scanf("%d",&n);
		for(int i=0; i<n; i++){
			scanf("%s",s);
			for(int j=0; j<n; j++)
				f[i][j] = s[j]=='1';
		}
		res=n*n;
		dfs(0,0,0);
		printf("Case #%d: %d\n",T,res);
	}
	return 0;
}
#include<stdio.h>
int tcn,tc;
int n;
char s[30][30];
int ans;
int mac[30];
void btrk(int dep,int used,int res){
	if(dep==0){
		if(res<ans)ans=res;
		return;
	}
	dep--;
	if(((used>>dep)&1)==0){
		int i,j,k,pn;
		for(i=(1<<dep);i<(1<<(dep+1));i++){
			if((used&i)!=0)continue;
			k=0;
			pn=0;
			for(j=0;j<=dep;j++){
				if(((i>>j)&1)!=0){
					pn++;
					k|=mac[j];
				}
			}
			for(j=0;j<=dep;j++){
				if(((i>>j)&1)==0){
					if(k&mac[j]){
						break;
					}
				}
			}
			if(j<=dep)continue;
			int t=0;
			for(j=0;j<n;j++){
				if(((k>>j)&1)!=0){
					t++;
				}
			}
			if(t>pn)continue;
			btrk(dep,used|i,res+pn*pn);
		}
	}
	else{
		btrk(dep,used,res);
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",s[i]);
			mac[i]=0;
			for(j=0;j<n;j++){
				if(s[i][j]=='1')mac[i]+=1<<j;
			}
		}
		ans=100000000;
		btrk(n,0,0);
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(s[i][j]=='1')ans--;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
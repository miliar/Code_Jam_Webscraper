#include <stdio.h>
#include <string.h>
int n,m,team[10],print[2],len[20];
char mun[10][20];
bool check[20];
int calc(int color){
	int i,j,cnt=0,k;
	for(i=0;i<m;i++){
		if(team[i]!=color) continue;
		memset(check,0,sizeof(check));
		for(j=0;j<i;j++){
			if(team[j]!=color) continue;
			check[0]=1;
			for(k=0;k<len[j] && k<len[i];k++){
				if(mun[i][k]==mun[j][k])
					check[k+1]=1;
				else break;
			}
		}
		for(j=0;j<=len[i];j++){
			if(!check[j])
				cnt++;
		}
	}
	return cnt;
}
void back(int k){
	int i;
	if(k==m){
		int sum=0,j;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if(team[j]==i) break;
			}
			if(j==m) return ;
		}
		for(i=0;i<n;i++){
			sum+=calc(i);
		}
		if(sum>print[0]){
			print[0]=sum;
			print[1]=0;
		}
		if(sum==print[0])
			print[1]++;
		return ;
	}
	for(i=0;i<n;i++){
		team[k]=i;
		back(k+1);
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test,testt,i;
	scanf("%d",&testt);
	for(test=1;test<=testt;test++){
		scanf("%d %d",&m,&n);
		for(i=0;i<m;i++){
			scanf("%s",mun[i]);
			len[i]=strlen(mun[i]);
		}
		print[0]=0;
		back(0);
		printf("Case #%d: %d %d\n",test,print[0],print[1]);
	}
	return 0;
}

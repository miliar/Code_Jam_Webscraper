#include<stdio.h>
int tcn,tc;
int n;
int chk[10];
int ans;
void digits(int x){
	while(x!=0){
		chk[x%10]=1;
		x/=10;
	}
}
int main(){
	int i,j;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",tc);
			continue;
		}
		for(i=0;i<10;i++)chk[i]=0;
		for(i=1;;i++){
			digits(i*n);
			for(j=0;j<10;j++){
				if(chk[j]==0)break;
			}
			if(j==10)break;
		}
		ans=i*n;
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}

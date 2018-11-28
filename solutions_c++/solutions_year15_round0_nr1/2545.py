#include<stdio.h>

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int N,sum=0,ans=0,a;
		scanf("%d",&N);
		for(int i=0;i<=N;i++){
			scanf("%1d",&a);
			if(a>0 && ans<i-sum)ans=i-sum;
			sum+=a;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
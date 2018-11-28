#include<stdio.h>
int main(){
	int T,SMAX,ans=0;
	char S[1002];
	
	long sum = 0;
	int i,j;
	scanf("%d",&T);
	for(i=0; i<T; i++){
		ans = 0;
		sum=0;
		scanf("%d %s ",&SMAX,S);	
		sum += S[0]-'0';
		for(j=1; j<=SMAX; j++){
			
			if(S[j]!='0' && j>sum){
				ans+= j-sum;
				sum+= j-sum;
			}
			sum+= S[j]-'0';
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}


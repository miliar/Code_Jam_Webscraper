#include<cstdio>

#define REP(i,n) for(int i=0;i<(n);i++)

int T,S;
char C[1050];

int main(){
	scanf("%d",&T);
	REP(i,T){
		scanf("%d%s",&S,&C);
		int sum=0,ans=0;
		REP(j,S+1){
		//	printf("%d:%d-%d\n",j,sum,ans);
			if(j>sum) {
				ans+=j-sum;
				sum+=j-sum;
			}
			sum+=(int)C[j]-48;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}			
	
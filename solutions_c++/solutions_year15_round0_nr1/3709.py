#include <cstdio>

int main(){
	
	char ch;
	int N,T;
	int ar[1010];
	scanf(" %d",&T);
	
	for(int i=1;i<=T;i++){
		scanf(" %d",&N);
		int res=0;
		for(int j=0;j<=N;j++){
			scanf(" %c",&ch);
			ar[j]=ch-'0';
		}
		for(int j=0;j<=N;j++)
			if(ar[j]>0)	
				ar[j+1]+=ar[j]-1;
			else res++;
		
		printf("Case #%d: %d\n",i,res);
	}

	return 0;
}

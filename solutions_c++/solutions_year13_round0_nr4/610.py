#include <stdio.h>
#include <string.h>
int N;
int chestType[201];
int K[201];
int keyTypes[201][401];
int M[1<<20];

int canOpen(int mask){
	int have[200];
	memset(have, 0, sizeof(have));
	for(int i=0;i<=N;++i){
		if((i==N) || (mask&(1<<i))){
			for(int j=0;j<K[i];++j){
				have[keyTypes[i][j]]++;
			}
			if(i<N){
				have[chestType[i]]--;
			}
		}
	}
	int co=0;
	for(int i=0;i<N;++i)if(!(mask&(1<<i))){
		if(have[chestType[i]]>0){
			co|=(1<<i);
		}
	}
	return co;
}

int solve(int mask){
	if(mask==((1<<N)-1)){
		return 0;
	}
	
	int &sol=M[mask];
	if(sol!=-1){
		return sol;
	}
	int co=canOpen(mask);
	for(int i=0;i<N;++i)if(co&(1<<i)){
		int op=solve(mask|(1<<i));
		if(op!=-2){
			return sol=i;
		}
	}
	return sol=-2;
}


int main(int argc, char *argv[]){
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;++c){
		scanf("%d%d", &K[0], &N);
		K[N]=K[0];
		for(int i=0;i<K[N];++i){
			scanf("%d", &keyTypes[N][i]);
		}
		for(int i=0;i<N;++i){
			scanf("%d%d", &chestType[i], &K[i]);
			for(int j=0;j<K[i];++j){
				scanf("%d", &keyTypes[i][j]);
			}
		}
		memset(M, -1, sizeof(M));
		int sol=solve(0);
		if(sol==-2){
			printf("Case #%d: IMPOSSIBLE\n", c);
		}else{
			printf("Case #%d:", c);
			int mask=0;
			while(mask!=((1<<N)-1)){
				printf(" %d", 1+M[mask]);
				mask|=(1<<M[mask]);
			}
			printf("\n");
		}
	}
	return 0;
}


#include <cstdio>
#include <cstring>
int N,f[10],TestCase;
void doit(){
	scanf("%d",&N);
	if(N==0){
		printf("INSOMNIA\n");
		return;
	}
	int R=0;
	memset(f,0,sizeof(f));
	for(int i=1; ; i++){
		int P=N*i;
		for( ; P; P/=10){
			int Q=P%10;
			if(!f[Q]) R++; f[Q]=1;
			if(R<10) continue;
			printf("%d\n", N*i);
			return;
		}
	}
}
		
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&TestCase);
	for(int O=1; O<=TestCase; O++){
		printf("Case #%d: ",O);
		doit();
	}
}


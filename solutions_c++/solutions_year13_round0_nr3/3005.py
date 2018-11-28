#include <cstdio>
int f[10000];
int main(){
	int T;
	f[1]=1;
	f[4]=2;
	f[9]=3;
	f[121]=4;
	f[484]=5;
	for(int i=1;i<=1000;++i)
		if(!f[i])f[i]=f[i-1];
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int A,B;
		scanf("%d%d",&A,&B);
		printf("Case #%d: %d\n",t,f[B]-f[A-1]);
	}
	return 0;
}
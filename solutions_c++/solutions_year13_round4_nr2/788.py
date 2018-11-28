#include<cstdio>
#include<algorithm>

using namespace std;

int N,P;

int zle(int x){
	int vys=0;
	for(int i=1;i<=N;++i){
		if ((1<<i)<=x+1){
			vys=(vys<<1)+1;
		}
		else{
			vys<<=1;
		}
	}
	return vys;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		printf("Case #%d: ",t);
		scanf("%d%d",&N,&P);
		int a=0,b=0;
		for(int i=0;i<(1<<N);++i){
			if (zle(i)<P){
				a=max(a,i);
			}
			if ((1<<N)-zle(i)-1<P){
				b=max(b,(1<<N)-i-1);
			}
		}
		printf("%d %d\n",a,b);
	}
	return 0;
}

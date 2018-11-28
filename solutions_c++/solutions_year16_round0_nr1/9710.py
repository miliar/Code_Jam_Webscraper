#include <stdio.h>
#include <cstring>
using namespace std;
bool h[10];
long long t,N,j,res;
void f(long long N){
	long long k = N;
	while(k){
		h[k%10] = true;
		k/=10;
	}
}
bool g(bool h[]){
	for(int i = 0;i<10; i++){
		if(h[i] == false) return true;
	}
	return false;
}
int main(){
	scanf("%lld",&t);
	for(int T = 1; T<=t; T++){
		memset(h,false,sizeof(h));
		res = 1LL;
		scanf("%lld",&N);
		printf("Case #%d: ",T);
		if(N == 0) printf("INSOMNIA\n");
		else{
			while(true){
				f(N*res);
				if(g(h)) res++;
				else break;
			}
			printf("%lld\n",res*N);

		}

	}
}
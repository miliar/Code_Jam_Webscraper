#include <stdio.h>
#include <algorithm>

using namespace std;

int N,X,S[10101];

void solve_case(){
	scanf("%d%d",&N,&X);
	for(int i=0;i<N;++i){
		scanf("%d",S+i);
	}
	sort(S,S+N);
	int vys=0;
	for(int a=0,b=N-1;a<=b;){
		if (a==b){
			++vys;
			break;
		}
		if (S[b]+S[a]<=X){
			++a;
		}
		--b;
		++vys;
	}
	printf("%d\n",vys);
}

int main(){
	int cases;
	scanf("%d",&cases);
	for(int t=1;t<=cases;++t){
		printf("Case #%d: ",t);
		solve_case();
	}
	return 0;
}


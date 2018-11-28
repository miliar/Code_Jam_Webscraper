#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int ntest;
int k,c,s;

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%d",&k);
	scanf("%d",&c);
	scanf("%d",&s);
	
	for(int i=0; i<k; i++){
		printf("%d ",i+1 );
	}
	printf("\n");
}

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d\n",&ntest);	
	for(int i=0;i<ntest; i++){
		solve(i);
	}
	return 0;
}
	
	
	

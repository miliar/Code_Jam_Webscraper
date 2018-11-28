#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

LL n;
int ntest;

void solve(int test){
	printf("Case #%d: ",test+1);
	scanf("%lld",&n);	
	if(!n){
		printf("INSOMNIA\n");
		return;
	}
	int vis=0;	
	LL cur=n;
	while( vis != (1<<10)-1){		
		LL temp = cur;		
		while(temp){
			vis |= 1<<(temp%10);
			temp/=10;
		}
		cur+=n;
	}
	printf("%d\n",cur-n);
}

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&ntest);	
	for(int i=0;i<ntest; i++){
		solve(i);
	}
	return 0;
}

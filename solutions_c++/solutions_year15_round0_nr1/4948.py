#include "baz.h"

int main(){
	int t, n;
	char bzn;
	scanf("%d", &t);
	REP(fn,t){
		scanf("%d", &n);
		int akt=0, ans=0;
		REP(i,n+1){
			cin>>bzn;
			if(akt<i)akt++, ans++;
			akt+=bzn-'0';
		}
		printf("Case #%d: %d\n", fn+1, ans);
	}
}
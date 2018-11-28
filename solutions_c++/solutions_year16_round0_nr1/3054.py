#include <bits/stdc++.h>
using namespace std;

int t,n;
bool used[10];

int main(){
	
	scanf("%d",&t);
	for( int tt = 1 ; tt <= t ; tt++ ){
		printf("Case #%d: ",tt);
		scanf("%d",&n);
		if( !n ){
			printf("INSOMNIA\n");
			continue;
		}
		memset(used , 0 , sizeof used);
		int ans = n;
		for( ;  ; ans += n ){
			int x = ans;
			while( x ){
				used[x % 10] = 1;
				x /= 10;
			}
			bool any = 0;
			for( int i = 0 ; i < 10 ; i++ )
				if( !used[i] ) any = 1;
			if( !any ) break;
		}
		printf("%d\n",ans);
	}
	return 0;
}

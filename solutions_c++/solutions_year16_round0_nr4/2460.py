#include <bits/stdc++.h>
using namespace std;

int t,k,c,s;

int main(){
	
	scanf("%d",&t);
	
	for( int tt = 1 ; tt <= t ; tt++ ){
		printf("Case #%d: ",tt);
		scanf("%d%d%d",&k,&c,&s);
		if( c == 1 ){
			if( s != k ){
				puts("IMPOSSIBLE");
				continue;
			}
			for( int i = 1 ; i <= s ; i++ ){
				if( i > 1 ) printf(" ");
				printf("%d",i);
			}
		} else {
			if( s + s < k ){
				puts("IMPOSSIBLE");
				continue;
			}
			for( int i = k ; i > k - s ; i-- ){
				if( i < k ) printf(" ");
				printf("%d",i);
			}
		}
		puts("");
	}
	
	return 0;
}

#include <bits/stdc++.h>
using namespace std;

int t;
char ar[110];

int main(){
	
	scanf("%d",&t);
	
	for( int tt = 1 ; tt <= t ; tt++ ){
		printf("Case #%d: ",tt);
		int ans = 0;
		scanf("%s",ar + 1);
		int n = strlen(ar + 1);
		while( true ){
			int i = 1;
			while( ar[i + 1] == ar[i] ) i++;
			if( i == n ) break;
			for( int j = 1 ; j <= i ; j++ )
				if( ar[j] == '+' ) ar[j] = '-';
				else ar[j] = '+';
			reverse(ar + 1 , ar + i + 1);
			ans++;
		}
		if( ar[n] == '-' )ans++;
		printf("%d\n",ans);
	}
	
	return 0;
}

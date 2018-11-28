#include<bits/stdc++.h>

using namespace std; 

const int MX = 1005; 

char t[MX]; 

int main () { 
	int q; 
	scanf("%d",&q);
	int repetition = 0; 
	while ( q-- ) {
		int n; 
		scanf("%d",&n); 
		scanf("%s",t); 
		int result = 0;
		int nowstanding = 0; 
		for ( int i = 0; i <= n; i++ ) {
			if ( nowstanding < i ) { 
				result += ( i - nowstanding );
				nowstanding = nowstanding + ( i - nowstanding ); 
			}
			nowstanding = nowstanding + (t[i]-'0');
		}
		printf("Case #%d: %d\n",++repetition,result); 
	}
}

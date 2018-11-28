#include <bits/stdc++.h>

using namespace std;
const int maxn = 1e2 + 15;
char str[maxn];

int main(int argc,char *argv[]){
	//freopen("in.txt" , "r" , stdin );
	//freopen("out.txt" , "w" , stdout );
	int Case , cas = 0;
	scanf("%d" , &Case );
	while(Case -- ){
		scanf("%s" , str + 1);
		int len = strlen( str + 1 );
		str[0] = str[1];
		int st = str[1] == '+' ? 0 : 1 , ans = 0;
		int i = 1;
		while( i <= len && str[i] == str[i - 1] ) ++ i;
		for(  ; i <= len ; ){
			int j;
			for(j = i ; j <= len && str[j] == str[i] ; ++ j);
			if( str[i] == '+' ){
				if( st == 1 ) st ^= 1 , ans ++ ;
			}else if( str[i] == '-' ){
				if( st == 0 ) st ^= 1 , ans ++;
			}
			i = j;
		}
		printf("Case #%d: %d\n" , ++ cas , ans + st );
	}
	return 0;
}
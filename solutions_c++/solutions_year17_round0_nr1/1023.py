#include <bits/stdc++.h>
using namespace std;
inline int read(){int x=0,f=1;char ch=getchar();while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}return x*f;}
const int maxn = 1000 + 50;
int n , K;
char s[maxn];

int main( int argc , char * argv[] ){
	//freopen( "in.txt" , "r" , stdin );
	//freopen( "out.txt" , "w" , stdout );
	int T = read() , cas = 0;
	while( T -- ){
		scanf( "%s%d" , s + 1 , & K );
		n = strlen( s + 1 );
		int ans = 0;
		for(int i = 1 ; i <= n - K + 1 ; ++ i)
			if( s[i] == '-' ){
				++ ans;
				for(int j = i ; j <= i + K - 1 ; ++ j)
					if( s[j] == '+' )
						s[j] = '-';
					else
						s[j] = '+';
			}
		printf( "Case #%d: " , ++ cas);
		int ok = 1;
		for(int i = 1 ; i <= n ; ++ i)
			if( s[i] == '-' ){
				ok = 0;
				break;
			}
		if( ok )
			printf( "%d\n" , ans );
		else
			printf( "IMPOSSIBLE\n" );
	}
	return 0;
}
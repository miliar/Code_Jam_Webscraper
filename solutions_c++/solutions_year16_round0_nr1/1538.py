#include <bits/stdc++.h>

using namespace std;

const int GoTime = 1e6;
const int Ed = ( 1 << 10 ) - 1 ;
int cal(long long x){
	if( x == 0 ) return 1;
	int res = 0;
	while( x ){
		res |= (1 << (x % 10));
		x /= 10;
	}
	return res;
}

int main(int argc,char *argv[]){
	//freopen("in.txt" , "r" , stdin );
	//freopen("out.txt" , "w" , stdout );
	int Case , cas = 0;
	scanf("%d",&Case);
	while(Case--){
		long long n , ans = -1 ;
		int res = 0 , add ; 
		scanf("%I64d",&n);
		add = n;
		for(int i = 1 ; i <= GoTime ; ++ i){
			res |= cal( n );
			if( res == Ed ){
				ans = n;
				break;
			}
			n += add;
		}
		printf("Case #%d: " , ++ cas);
		if( ans == -1 ) printf("INSOMNIA\n");
		else printf("%I64d\n",ans);
	}
	return 0;
}
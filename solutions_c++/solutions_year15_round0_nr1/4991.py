# include <stdio.h>
# include <iostream>
using namespace std;

int test( string s, long long x ){
	for( int i = 0; i < s.size(); i++ ){
		if( x < i ) return 0;
		else x = x + s[i] - 48;
	}
	return 1;
}

long long search( string s ){
	long long l = -1, h = 1000000;
	while( h - l > 1){
		long long mid = ( l + h )/2;
		if( test( s, mid) ){
			h = mid;
		}
		else 
			l = mid;
	} 
	return h;
}

int main(){
    freopen("input.txt", "r" , stdin );
    freopen("output.txt", "w" , stdout );
	int t;
	scanf("%d",&t);
	for( int kr = 1; kr <= t; kr++ ){
		printf("Case #%d: ",kr);
		int n; scanf("%d",&n);
		string s;
		cin>>s;
		printf("%lld\n",search(s));
	}
	return 0;
}

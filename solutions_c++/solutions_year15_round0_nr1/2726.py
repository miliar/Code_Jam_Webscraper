#include<bits/stdc++.h>
using namespace std;
string s;

int main(){
	int tc, n , caso = 0;
	cin>>tc;
	while( tc--){
		cin>>n >>s ;
		n++;
		int sum =0, ans = 0;
		for( int i =0 ; i<n ; ++i ){
			if( sum < i ) ans += ( i - sum ) , sum = i;
			sum += (s[ i ]-'0');
		}
		printf("Case #%d: %d\n" , ++caso , ans );
	}
}

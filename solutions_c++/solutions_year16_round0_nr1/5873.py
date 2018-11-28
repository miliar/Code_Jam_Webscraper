#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
	int n;
	cin>>n;
	ll maxi = 0;
	for ( int i = 0 ; i < n ; i++ ){
		ll x;
		cin>>x;
		vector< int > VIS( 10 , 0 );
		int cnt = 10;
		if ( x == 0 ){
			printf("Case #%d: INSOMNIA\n",i+1);
		}else{
			ll p = 1;
			while ( x ){
				ll val = p*x;
				ll cur = val;
				while ( cur ){
					ll dig = cur%10LL;				
					cur /= 10LL;
					if ( VIS[ dig ] == 0 ){
						VIS[ dig ] = 1;
						cnt--;
					}
					if ( cnt == 0 ) break;  
				}											 
				if ( cnt == 0 ){
					printf("Case #%d: %lld\n",i+1,p*x);
					break;
				}		
				p++;
			}
		}
	}
}

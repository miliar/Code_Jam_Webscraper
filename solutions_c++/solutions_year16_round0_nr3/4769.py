#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
	int T;
	cin>>T;
	int n , cnt;
	printf("Case #%d:\n",1);
	for ( int tt = 0 ; tt < T; tt++ ){
			cin>>n>>cnt;
			for ( int k = 0 ; k <(1LL<<n ); k++ ){
				if ( cnt == 0 ) break;
				bool ok = 1;
				vector< ll > pal;
				for ( int j = 2; j <= 10; j++ ){

					if ( !(k & ( 1 << ( n - 1 ) ) ) ){
						ok = 0;
						break;
					}
					if ( !( k & ( 1 << 0 ) ) ){
						ok = 0;
						break;
					}
					
					
					ll sum = 0;
					
					for ( int l = n - 1 ; l >= 0 ; l-- ){
						if ( k & ( 1 << l ) ){
							sum = sum*j + 1;
						}else sum = sum*j;			
					}					
					ll d = -1;
					bool primo = 1;
					for ( ll pp = 2 ; pp*pp <= sum ; pp++ ){
						if ( sum % pp == 0 ){
							primo = 0;
							d = pp;
						}						
					}
					if ( primo ){ ok = 0;break;}
					else pal.push_back( d );
				}
				if ( ok ){ 
					for ( int l = n - 1; l >= 0 ;l-- ){
						if ( k & ( 1 << l ) ){
							cout<<1;
						}else cout<<0;
					}
					cnt--;
					cout<<" ";
					for ( int l = 0 ; l < 9 ; l++ ) cout<<pal[ l ]<<char( l + 1 == 9 ? 10 : 32 );
				}
			}
		
	}
/*
	2^n + x + 1
	
	3^n + y + 1
	
	4^n + z + 1
	
	10^n + w + 1
		
	cout<<pow( 2 , 14 )*9*10<<endl;
*/
}

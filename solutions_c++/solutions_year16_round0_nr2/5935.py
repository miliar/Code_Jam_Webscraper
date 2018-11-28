#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	string s;
	int ans = 0;
	for ( int i = 0 ; i < n; i++ ){
		cin>>s;
		int tam = (int)s.size();
		char car = s[ 0 ];
		int ans = 0;
		for ( int j = 1 ; j <= tam; j++ ){
			if ( j == tam ){
				if ( car == '-' ) ans++;
			}else{
				if ( s[ j ] != car ){
					car = s[ j ];
					ans++;
				}
			}
		}	
		printf("Case #%d: %d\n",i+1 , ans);
	}
}

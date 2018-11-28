#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int T,N,ar[1100];

int main(){
	
	cin >> T;

	for( int z=1 ; z<=T ; z++ ){
		cin >> N;
		char c;
		for( int i=0 ; i<=N ; i++ ){
			scanf(" %c",&c);
			ar[i]=c-'0';
		}
		int res=0,size=0;
		for( int i=0 ; i<=N ; i++ ){
			if( size >= i ) size+=ar[i];
			else if( ar[i] ) res+=i-size,size=i+ar[i]; 
		}
		printf("Case #%d: %d\n",z,res);
	}

}
//~ gango reyiz

#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

const int MAXN=1024;

int S,K;
int ar[MAXN];

int main(){
	
	scanf("%d",&K);
	
	for( int C=1 ; C<=K ; C++ ){
		
		int r=0,c=0;
		char ch;
		
		scanf("%d",&S);
		
		for( int i=0 ; i<=S ; i++ ){
			scanf(" %c",&ch);
			ar[i]=ch-'0';
		}
		
		c=ar[0];
		for( int i=1 ; i<=S ; i++ ){
			if( ar[i] && i>c ){
				r+=i-c;
				c+=i-c;
			}
			c+=ar[i];
		}
		
		printf("Case #%d: %d\n",C,r);
	}
	
	return 0;
}
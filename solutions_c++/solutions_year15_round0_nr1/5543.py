//~ gedemenli

#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int S,K;
int arr[100100];

int main(){
	
	scanf("%d",&K);
	
	for( int C=1 ; C<=K ; C++ ){
		
		int ans=0,c=0;
		char ch;
		
		scanf("%d",&S);
		
		for( int i=0 ; i<=S ; i++ ){
			scanf(" %c",&ch);
			arr[i]=ch-'0';
		}
		
		c=arr[0];
		//~ cout << c << endl;
		
		for( int i=1 ; i<=S ; i++ ){
			if( arr[i] && i>c ){
				ans+=i-c;
				c+=i-c;
			}
			c+=arr[i];
		}
		
		printf("Case #%d: %d\n",C,ans);
	}
	
	return 0;
}
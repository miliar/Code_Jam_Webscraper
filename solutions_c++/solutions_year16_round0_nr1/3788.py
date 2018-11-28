#include <bits/stdc++.h>

#define db 	cout << "*****" << endl;
#define Max 100009
#define pb push_back
#define pp pop_back
#define ff first
#define ss second
#define mk make_pair
#define MOD 1000000007

using namespace std;

int n;

int arr[15];

int main(){
	
	int t=0;
	
	freopen("1.in" , "r" , stdin);
	freopen("1.out" , "w" , stdout);
	
	scanf("%d" ,&t);
	
	for( int i=1;i<=t;i++){
		long long a;
		
		scanf("%lld" ,&a);
		
		memset( arr , 0 , sizeof arr );
		int jog=10;
		
		if( a == 0 ){
			printf("Case #%d: INSOMNIA\n",i);
			continue;	
		}
		
		for( int j=1;j<=100000000000000000;j++){
			long long b = a * j * 1LL;
			while( b > 0 ){
				int c = b % 10 ;
				if( arr[c] == 0 ){
					arr[c] = 1 ;
					jog--;	
				}
				b/=10;
			}	
			if( jog == 0 ){
				printf("Case #%d: %lld\n",i , a * j * 1LL);
				break;	
			}
		}	
			
	}
	return 0;
}

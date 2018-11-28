#include<bits/stdc++.h>
#define ll long long
using namespace std;
int casos = 0, cant = 0;
bool flag[ 10 ];

void process( ll n ){
	while( n>0 ){
		int d = n%10;
		if( !flag[ d ] ){
			flag[ d ] = 1;
			cant++;
		}
		n/=10;
	}
}


void doit(){
	int n;
	scanf("%d", &n );
	printf("Case #%d: ", ++casos );
	if( n==0 ){
		puts("INSOMNIA");
		return;
	}
	memset( flag, 0 , sizeof(flag ) );
	cant = 0;
	for( ll i=1 ; ; ++i ){
		ll cur = n*i;
		process( cur );
		if( cant == 10 ){
			printf("%lld\n", cur );
			break;
		}
	}
}


int main(){
	int tc;
	scanf("%d", &tc );
	while( tc-- ) doit();
}

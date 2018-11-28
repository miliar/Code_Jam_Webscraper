#include <bits/stdc++.h>
#include <string>
#define ll long long
using namespace std;
bool arr[10];
string s;
bool check(){
        for( int i=0 ; i<10 ; ++i )
                if( !arr[i] )
                        return true;
        return false;
}
int main(){
	int t, i, j;
	ll n, m, p;
	scanf( "%d", &t );
    	for( int kj=1 ; kj<=t ; ++kj ){
                scanf("%lld", &n);
                memset( arr, 0, sizeof arr);
                printf("Case #%d: ", kj);
                if( n == 0 ) {
                        printf("INSOMNIA\n");
                        continue;
                }
                m = n;
                j=1;
                while( check() ){
                        m = n * j++;
                        while( m ){
                                p = m%10;
                                arr[p] = true;
                                m /= 10;
                        }
                }
                printf("%lld\n", n *(j-1) );
    	}
    	return 0;
}

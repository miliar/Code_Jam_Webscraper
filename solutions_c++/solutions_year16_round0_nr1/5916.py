#include <algorithm>
#include <cstdio>
#include <cstring>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end()
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
bool H[10];
void solve( long long n ) {

	memset( H , 0 , sizeof H );
	long long a = n;
	int s(0);

	while(1) {

		if( n <= 0 ) break;

		long long t = n;
		while(t) {
			if( !H[t%10] && ++s == 10 ) {
				printf("%lld\n" , n );
				return;
			}
			H[t%10] = true;
			t /= 10;
		}

		n += a;

	}

	printf("INSOMNIA\n");

}
int main()
{
	freopen( "input.txt" , "r" , stdin );
	freopen( "output.txt" , "w" , stdout );
	int T = read(),i;
	FOR(i,1,T) {
		printf("Case #%d: " , i );
		solve( read() );
	}
	return 0;
}

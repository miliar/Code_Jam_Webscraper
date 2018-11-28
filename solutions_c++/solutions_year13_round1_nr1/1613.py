#include <cstdio>

#define FOR(i,a,b) for (int i=(a);i<(b);i++) 
#define SZ(x) ((int)x.size()) 

using namespace std;

int main () {

	long long int T, t, r;
	long long int left, rad, quant;
	
	scanf("%lld", &T);
	
	FOR(cc,0,T) {
		scanf("%lld %lld", &r, &t);
		left = t;
		rad = r+1;
		quant = 0;
		while ( true ) {
			left -= 2*rad - 1;
			
			if ( left < 0 ) break;
			
			rad += 2;
			quant++;
		}
		
		printf("Case #%d: %lld\n", cc+1, quant);
	}
	
	return 0;

}

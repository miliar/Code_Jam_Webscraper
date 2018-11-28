#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <list>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <ctime>

using namespace std;

#define MAX 10001000
#define INF 1000000
#define EPS 1e-7
#define PI acos(-1.0)
#define READ() freopen("input_B.txt", "r", stdin)
#define WRITE() freopen("output_B.txt", "w", stdout)
#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )
#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

int cf[MAX];

void itos(long long int x, char *s){
	sprintf(s, "%lld", x);
}

bool ispal(long long int x){
	char s[20];
	itos(x, s);
	int len = strlen(s);
	int l = len / 2;
	for(int i=0; i<l; i++){
		if( s[i] != s[len-1-i] ) return false;
	}
	return true;
}

void preprocess(){
	cf[0] = 0;
	for(long long int i=1; i<MAX; i++){
		cf[i] = cf[i-1];
		if( ispal(i) && ispal(i*i) ){
			//printf("%lld %lld\n", i, i*i);
			cf[i]++;
		}
	}
}

int main(){
	preprocess();
	//ios_base::sync_with_stdio(false);
	READ();
	WRITE();
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		long long int x, y;
		scanf("%lld %lld", &x, &y);
		long long int sx = ceil( sqrt((double)x) );
		long long int sy = floor( sqrt((double)y) );
		printf("Case #%d: %d\n", t, cf[sy] - cf[sx-1]);
	}
	return 0;
}



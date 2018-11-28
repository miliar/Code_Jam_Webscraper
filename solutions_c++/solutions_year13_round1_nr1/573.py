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

#define MAX 1001
#define INF 1000000
#define EPS 1e-7
#define PI acos(-1.0)
#define READ() freopen("Ainput.txt", "r", stdin)
#define WRITE() freopen("Aoutput.txt", "w", stdout)
#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )
#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

int main(){
	READ(); WRITE();
	//ios_base::sync_with_stdio(false);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		unsigned long long int r, tt;
		scanf("%llu %llu", &r, &tt);
		unsigned long long int res = 0;
		unsigned long long int low = 0;
		unsigned long long int high = 10000;
		while(low <= high){
			unsigned long long int mid = (low+high) / 2;
			unsigned long long int x = 2 * r * mid + mid * (2 * 1 + (mid-1) * 4) / 2;
			//printf("%llu %llu %llu %llu\n", low, high, mid, x);
			if( x <= tt ){
				res = mid;
				low = mid + 1;
			}
			else{
				high = mid - 1;
			}
		}
		printf("Case #%d: %llu\n", t, res);
	}
	return 0;
}


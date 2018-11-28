#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int reverse( int n ) {
    int ret = 0;

    while( n ) {
	ret = ret * 10 + (n % 10);
	n /= 10;
    }
    
    return ret;
}

int main( void ) {
    int T;
    scanf("%i", &T);
    
    const int MAX = (int) 1e6 + 10;

    int dist[MAX + 100], visited[MAX + 100];

    memset(visited, 0, sizeof(visited));
    queue<int> Q;

    Q.push(0);
    dist[0] = 0;

    while( !Q.empty() ) {
	int n = Q.front(); Q.pop();

	if( (n + 1) <= MAX && !visited[n + 1] ) {
	    visited[n + 1] = 1;
	    dist[n + 1] = dist[n] + 1;

	    Q.push(n + 1);
	}

	if( reverse(n) <= MAX && !visited[ reverse(n) ] ) {
	    visited[ reverse(n) ] = 1;
	    dist[ reverse(n) ] = dist[n] + 1;

	    Q.push( reverse(n) );
	}
    }
    
    for( int t = 1; t <= T; t++ ) {
	int target;
	scanf("%i", &target);
	
	printf("Case #%i: %i\n", t, dist[target]);
    }

    return 0;
}

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int MUL[5][5] = {
        {0, 0, 0, 0, 0},
	    {0, 1, 2, 3, 4},
	        {0, 2, -1, 4, -3},
		    {0, 3, -4, -1, 2},
		        {0, 4, 3, -2, -1}
};

int sign( int n ) {
        return (n <= 0) ? -1 : 1;
}

int mul( int n, int m ) {
        int sgn = sign(n) * sign(m);
	    return sgn * MUL[abs(n)][abs(m)];
}

int ctoi( int c ) {
        return c - 'i' + 2;
}

int main( void ) {
    int T;
    scanf("%i", &T);
    
    int nC = 1;
    while( T-- ) {
	string t; int N, X;
	cin >> N >> X >> t;

	string s; 
	for( int i = 1; i <= X; i++ )
	    s += t;
	
	int i, I = 0, J = 0, K = 0;

	int cur = 1;
	for( i = 0; i < X * N; i++ ) {
	    cur = mul(cur, ctoi(s[i]));

	    if( cur == 2 ) {
		I = 1;
		break;
	    }
	}

	cur = 1;
	for( i += 1; i < X * N; i++ ) {
	    cur = mul(cur, ctoi(s[i]));

	    if( cur == 3 ) {
		J = 1;
		break;
	    }
	}
	
	cur = 1;
	for( i += 1; i < X * N; i++ )
	    cur = mul(cur, ctoi(s[i]));
	
	if( I && J && (cur == 4) ) 
	    printf("Case #%i: YES\n", nC++);
	else	
	    printf("Case #%i: NO\n", nC++);
	    
    }

    return 0;
}

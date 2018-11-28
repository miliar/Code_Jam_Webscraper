#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
	
	freopen( "b.in", "r", stdin );
	freopen( "SalidaB.txt", "w", stdout );
	
	int tc, ntc = 0;
	double C, F, X, nc;
	
	scanf("%d", &tc);
	
	while ( tc -- ) {
		ntc ++;
		
		cin >> C >> F >> X;
		
		nc = 2.0;
		
		double acum = 0.0, ant = X / 2.0, sig;
		
		while ( true ) {
			sig = acum + C / nc;
			acum += C / nc;
			nc += F;
			sig += X / nc;
			if ( sig > ant ) break;
			ant = sig;
		}
		
		
		printf("Case #%d: %.8lf\n", ntc, ant);
	}

	return 0;
}


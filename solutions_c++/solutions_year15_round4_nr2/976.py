#include <bits/stdc++.h>
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)

#define epsilon (1e-20)

// Premature optimization is the root of all evil

using namespace std;


void solveacase() {

	int N;
	double V, X;
	cin >> N >> V >> X;
	double R[N];
	double T[N];

	forn(i, N){
		cin >> R[i] >> T[i];
	}

	assert ( N < 3 );

	if ( N == 1 ) {
		if ( T[0] == X ) {
			cout << V / R[0] << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
		return;
		
	}

	if ( X == T[0] ) {
		if ( X == T[1] ) {
			cout << V / (R[0]+R[1]) << endl;
		}
		else {
			cout << V / R[0] << endl;
		}
		return;
	}
	if ( X == T[1] ) {
		cout << V / R[1] << endl;
		return;
	}

	double p = (X - T[1]) / (T[0] - T[1]);
	double time = max ( p * V / R[0], (1-p) * V / R[1] );

	if ( -epsilon <= p && p <= 1+epsilon ) {
		cout << time << endl;
	}
	else {
		cout << "IMPOSSIBLE" << endl;
	}

	return;
}

int main ( int, char** ) {

	int T;
	cin >> T;

	for ( int i = 1; i <= T; ++i ) {
		cout << "Case #" << i << ": " << setprecision(12);
		solveacase();
	}


	return 0;
}

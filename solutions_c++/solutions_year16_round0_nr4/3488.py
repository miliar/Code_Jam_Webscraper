#include <iostream>
#include <vector>
#include <string>

using namespace std;

void do_case() {
	unsigned int K, C, S;
	cin >> K >> C >> S;

	if( K == S ) {
		for( unsigned int i=1; i<=K; ++i ) {
			cout << i << " ";
		}
	}

	/*
	if( K <= C*S ) {
		for( int i=0; i*C<=K; ++i ) {
		}
	}
	else {
		cout << "IMPOSSIBLE";
	}
	*/
}

int main() {
	int T;
	cin >> T;

	for( int i=0; i<T; ++i ) {
		cout << "Case #" << (i+1) << ": ";
		do_case();
		cout << endl;
	}
}

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int main() {
	FILE *fin = freopen("D-small-attempt1.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("D-small-attempt1.out", "w", stdout);
	int T,K,C,S;
	cin >> T;


	for(int t = 1; t <= T; t++){
		// Get the pancake stack		
		//pstack.clear();
		cin >> K >> C >> S;
//		cout << "[" << K << " " << C << " " << S << "] ";

		// Process it
		if (K>=2*S) {
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		} else {

			long int N=1;
			for (int c=0; c<C; c++)
				N *= K;

			cout << "Case #" << t << ":";
			for (int s=0; s<S; s++) {
				long int i = s*K + (K-s);
				
				if (i<=N) {
					cout << " " << i;
				} else {
					cout << " " << N-s;
				}
			}
			cout << endl;
		}
		
		//cout << "Case #" << t << ": " << x << endl;
	}
	return 0;
}

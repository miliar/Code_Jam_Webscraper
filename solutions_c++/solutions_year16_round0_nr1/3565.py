#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T,N;
	cin >> T;
	for(int t = 0; t < T; t++){
		// Get the number		
		cin >> N;

		// Process it
		int x = -1;
		bool seen[10] = {false,false,false,false,false,false,false,false,false,false};
		int nb_unseen=10;
		int n=0, d=0;	
		// Only N=0 is impossible
		if (N>0) {
			x = 0;

			while (1) {	
				// Split the number
				n = N*(x+1);

				// Check the digits
				while(n>0) {
					d = n%10;
		
					if (!seen[d]) {
						// Change to seen
						seen[d] = true;
						// Decrement the number of digits left and stop if 0
						if (--nb_unseen == 0)
							break;
					}
					n = n/10;
				} 
				if (nb_unseen == 0)
					break;
				x++;
			}
			cout << "Case #" << t+1 << ": " << N*(x+1) << endl;
		} else {
			// Impossible
			cout << "Case #" << t+1 << ": INSOMNIA"  << endl;
		}
		
		
	}
	return 0;
}

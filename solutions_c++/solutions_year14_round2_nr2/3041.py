#define N 4

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main (void)
{
	int T; 						// number of games
	int A, B, K;
	
	cin >> T;
	
	for (int t = 0; t < T; t++) {

		cin >> A >> B >> K;

		int counter = 0;
		for (int i = 0; i < A; i++) {
			for (int j = 0; j < B; j++) {
				if ((i & j) < K) counter++;
				
			}
		}
		
		// Output
		cout << "Case #" << t+1 << ": "; 
		cout << counter << endl;
	}
		
	return 0;	
}
			
#include <iostream>

using namespace std;

int main(int argc, char ** argv) 
{
	int T;
	cin >> T;
	for(int tcase = 1; tcase <= T; tcase++) {
		int A, B, K;
		cin >> A >> B >> K;
		// brute force
		int ncount = 0;
		for(int k = 0; k < K; k++) {
			for(int a = 0; a < A; a++) {
				for(int b = 0; b < B; b++) {
					if((a & b) == k)
						ncount++;
				}
			}
		}
		cout << "Case #" << tcase << ": " << ncount << endl;
	}
	return 0;
}
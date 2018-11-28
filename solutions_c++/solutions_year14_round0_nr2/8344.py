#include <iostream>

using namespace std;

int main() {
	int numTest;

	cin >> numTest;

	for (int i=0; i<numTest; i++) {
		double C, F, X;

		cin >> C >> F >> X;

		int count = 0;
		double prev = INT_MAX, curr=INT_MAX;

		do {
			prev = curr;

			curr = 0;
			for (int j=0; j<count; j++) {
				curr += C/(2+j*F);
			}
			curr += X/(2+count*F);

			count++;
		} while (prev > curr);

		printf("Case #%i: %lf\n", i+1, prev);
	}
}
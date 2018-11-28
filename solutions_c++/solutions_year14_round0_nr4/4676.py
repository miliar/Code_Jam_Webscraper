#include <iostream>
#include <algorithm>

double A[1010], B[1010];
bool V[1010];

int main() {
	int z;
	std::cin >> z;

	for (int i=1; i<=z; i++) {
		int n;
		std::cin >> n;
		
		for (int j=0; j<n; j++) std::cin >> A[j];
		for (int j=0; j<n; j++) {
			std::cin >> B[j];
			V[j] = false;
		}

		std::sort(A, A+n);
		std::sort(B, B+n);

		int result = 0;

		for (int j=0; j<n; j++) {
			int it = -1;

			for (int k=0; k<n; k++) {
				if (!V[k] && A[j]-B[k]>0.000001) {
					it = k;
				}
			}

			if (it >= 0) {
				V[it] = true;
				result++;
			} else {
				for (int k=n-1; k>=0; k--) {
					if (!V[k]) {
						V[k] = true;
						break;
					}
				}
			}

		}

		int result1 = 0;

		for (int j=0; j<n; j++) V[j] = false;

		for (int j=n-1; j>=0; j--) {
			int it = -1;

			for (int k=0; k<n; k++) {
				if (!V[k] && A[j] - B[k] < 0.000001) {
					it = k;
					break;
				}
			}

			if (it >= 0) {
				V[it] = true;
			} else {
				result1++;
				for (int k=0; k<n; k++) {
					if (!V[k]) {
						V[k] = true;
						break;
					}
				}
			}
		}

		std::cout << "Case #" << i << ": " << result << " " << result1 << std::endl;
	}
}
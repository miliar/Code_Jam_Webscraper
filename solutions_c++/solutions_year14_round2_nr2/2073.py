#include <fstream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main(int argc, char** argv) {
	ifstream ifile(argv[1]);
	ofstream ofile(argv[2]);

	int T; ifile >> T;
	for (int tc = 1; tc <= T; tc++) {
		long int A; ifile >> A;
		long int B; ifile >> B;
		long int K; ifile >> K;
		
		long int min = 0;
		for (long int k = 0; k < K; k++) {
			for (long int a = 0; a < A; a++) {
				for (long int b = 0; b < B; b++) {
					long int m = a & b;
					if (m == k) {
						//if (a != b && b < A) {
							//min++;
						//}
						min++;
					}
				}
			}
		}

		ofile << "Case #" << tc << ": " << min << endl;
	}

	return 0;
}
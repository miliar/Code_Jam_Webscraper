#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int main() {
	int test_cases;
	cin >> test_cases;
	
	vector<int> res(test_cases, 0);
	
	for (int i = 0; i < test_cases; i++) {
		int A,B,K;
		cin >> A >> B >> K;
		
		for (int j = 0; j < A; j++) {
			for (int k = 0; k < B; k++) {
				int r = j&k;
				if (r < K) {
					res[i]++;
				}
			}
		}
	}

	int c = 1;
	for (int i = 0; i < test_cases; i++) {
		cout << "Case #" << c << ": " << res[i] << endl;
		c++;
	}
	return 0;
}


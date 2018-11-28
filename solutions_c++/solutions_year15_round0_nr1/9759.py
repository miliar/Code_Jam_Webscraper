#include <iostream>
#include <string>

using namespace std;

int main() {
	int t = 0;
	cin >> t;
	cin.get();

	int smax = 0;
	int count = 0;
	string audience = "";
	int levels[1001];
	string convert;
	int sum = 0;
	for (int i = 1; i <= t; i++) {
		// INPUT
		smax = 0;
		audience = "";
		count = 0;

		cin >> smax;
		getline(std::cin, audience);

		for (int j = 0; j <= smax; j++) {
			convert = audience[j+1];
			levels[j] = atoi(convert.c_str());
		}

		// PROCESS TEST CASE
		for (int j = 1; j <= smax; j++) {
			sum = 0;

			for (int k = 0; k < j; k++) {
				sum = sum + levels[k];
			}

			if (sum < j) {
				count = count + (j - sum);
				levels[j-1] = levels[j-1] + (j - sum);
			}
		}

		// OUTPUT RESULT
		cout << "Case #" << i << ": " << count << endl;
	}

	return 0;
}
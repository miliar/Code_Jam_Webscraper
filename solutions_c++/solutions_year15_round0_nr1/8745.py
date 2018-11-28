#include <iostream>
#include <vector>

using namespace std;

int main() {
	unsigned short number_of_test_cases;
	cin >> number_of_test_cases;

	for(unsigned short test_case = 0;
			test_case < number_of_test_cases;
			++test_case) {
		vector<int> S;
		size_t audience_size;
		cin >> audience_size;
		cin.get(); // Ignore the space
		for(size_t i = 0; i <= audience_size; ++i)
			S.push_back((int)(cin.get() - '0'));
		cin.get();
		// END OF INPUT READ
		int friends_invited = 0;
		int people_standing = S[0]; // People who stand regardless
		for(int i = 1; i < S.size(); ++i) {
			if(people_standing < i) {
				int hold = i - people_standing;
				friends_invited += hold;
				people_standing += hold;
			}
			people_standing += S[i];
		}

		cout << "Case #" << test_case + 1 << ": " << friends_invited << endl;
	}
	return 0;
}

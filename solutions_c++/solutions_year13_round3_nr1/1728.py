#include <iostream>
using namespace std;

inline bool isVowel(char c) {
  return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main(void) {
	int T, n;
	string name;

	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> name >> n;

		int nValue = 0, stopStart = -1;
		for (int i = 0, size = name.size(); i <= size - n; i++) {
			bool isCandidate = true;

			for (int j = 0; j < n; j++) {
				if (isVowel(name[i + j])) {
					isCandidate = false;
					break;
				}
			}

			if (isCandidate) {
				nValue += max(1, i - stopStart) * max(0, size - i -n + 1);
				stopStart = i;
			}
		}

		cout << "Case #" << t << ": " << nValue << endl;
	}
}
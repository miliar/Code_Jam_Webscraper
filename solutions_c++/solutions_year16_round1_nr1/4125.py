#include <iostream>
#include <bitset>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	char S[1024];
	char answer[1024];
	int len;
	vector<char> answer_string;

	for (int i = 0; i < T; ++i) {
		cin >> S;
		len = strlen(S);

		char lastChar = 'A';
		for (int j = 0; j < len; ++j)
		{
			if (S[j] > lastChar) {
				lastChar = S[j];
			}
		}

		cout << "Case #" << i + 1 << ": ";
		int maxCount = 0;
		int p = 0;
		bool maxSeen = false;

		for (int j = 0; j < len; ++j) {
			if (S[j] == lastChar) {
				++maxCount;
				maxSeen = true;
			}
			else if (answer_string.size() == 0) {
				answer_string.push_back(S[j]);
			}
			else {
				char head = answer_string.at(0);
				if (head <= S[j] && !maxSeen) {
					answer_string.insert(answer_string.begin(), S[j]);
					
				}
				else {
					answer_string.push_back(S[j]);
				}
			}
		}

		for (int j = 0; j < maxCount; ++j) {
			answer_string.insert(answer_string.begin(), lastChar);
		}

		for (int j = 0; j < answer_string.size(); ++j) {
			cout << answer_string.at(j);
		}

		answer_string.clear();

		cout << endl;
	}

	return 0;
}
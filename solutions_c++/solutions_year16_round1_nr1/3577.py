#include <iostream>
#include <vector>

using namespace std;

void solve(int C, char* word, int size) {
	vector<char> solved;
	cout << "Case #" << C << ": ";
	solved.push_back(word[0]);
	for (int i = 1; i < size; ++i) {
		if (word[i] >= solved.at(0)) {
			solved.insert(solved.begin(), word[i]);
		} else {
			solved.push_back(word[i]);
		}
	}
	for (vector<char>::iterator it = solved.begin(); it < solved.end(); it++) {
		cout << *it;
	}
	cout << endl;
}

int main(int argc, char* argv[]) {
	int T;
	char word[1001];
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cin >> word;
		solve(i + 1, word, strlen(word));
	}
	return 0;
}
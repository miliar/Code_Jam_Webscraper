#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <string>

using namespace std;

char flip(char ch) {
	switch (ch) {
	case '+': return '-';
	case '-': return '+';
	default: return ch;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		string pancakes;
		int K;
		cin >> pancakes >> K;
		int flips = 0;
		for (int i = 0; i < pancakes.size() - K + 1; ++i) {
			if (pancakes[i] == '-') {
				++flips;
				for (int j = 0; j < K; ++j) {
					pancakes[i + j] = flip(pancakes[i+j]);
				}
			}
			else if (pancakes[i] != '+') {
				cerr << "INVALID PANCAKE!" << endl;
			}
		}
		bool allsmiles = true;
		for (int i = 0; i < pancakes.size(); ++i) {
			if (pancakes[i] != '+') allsmiles = false;
		}
		cout << "Case #" << casen << ": ";
		if (allsmiles) cout << flips; else cout << "IMPOSSIBLE";
		cout << '\n';
	}
	return 0;
}


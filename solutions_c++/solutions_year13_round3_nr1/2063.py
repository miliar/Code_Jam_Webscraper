#include <iostream>
#include <map>
#include <vector>
using namespace std;

struct rangePair {
	int start, end;
};

int find(string name, int start, int now, map<char, bool>& vowel) {
	if (start <= now) {
		if (vowel[name[now]])
			return now;
		else
			return find(name, start, now - 1, vowel);
	}
	else
		return -1;
}

int main() {
	int n;
	map<char, bool> vowel;

	vowel['a'] = true;
	vowel['e'] = true;
	vowel['i'] = true;
	vowel['o'] = true;
	vowel['u'] = true;

	cin >> n;
	for (int i=1; i<=n; i++) {
		string name;
		int least, start, end;
		int valueCount = 0;
		vector<struct rangePair*> ranges;

		cin >> name >> least;
		start = 0;
		end = start + least - 1;
		while (end < name.length()) {
			int vowelPos;

			vowelPos = find(name, start, end, vowel);
			if (vowelPos == -1) {
				struct rangePair* thePair = new struct rangePair;

				thePair->start = start;
				thePair->end = end;
				ranges.push_back(thePair);
				start++;
				end++;
			}
			else {
				start = vowelPos + 1;
				end = start + least - 1;
			}
		}

		for (int j=least; j<=name.length(); j++) {
			int testEnd;

			for (int k=0;; k++) {
				testEnd = k + j - 1;
				if (testEnd < name.length()) {
					for (int m=0; m<ranges.size(); m++)
						if (k <= ranges[m]->start && testEnd >= ranges[m]->end) {
							valueCount++;
							break;
						}
				}
				else
					break;
			}
		}
		cout << "Case #" << i << ": " << valueCount << endl;
	}

	return 0;
}

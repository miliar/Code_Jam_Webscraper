#include <iostream>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

int words;
map<string, int> wordid;

inline int getID(const string& word) {
	auto it = wordid.find(word);
	if (it != wordid.end()) return it->second;
	return wordid[word] = words++;
}

bool knownEnglish[5000];
bool knownFrench[5000];

vector<int> commonLang[5000];

int matchedEng[5000];
int matchedFre[5000];

bool visitedEng[5000];
bool visitedFre[5000];

bool augmentFre(int id);

bool augmentEng(int id) {
	if (knownEnglish[id] || visitedEng[id]) return false;
	visitedEng[id] = true;

	for (int id2 : commonLang[id]) {
		if (id2 != matchedEng[id] && augmentFre(id2)) {
			matchedEng[id] = id2;
			matchedFre[id2] = id;
			return true;
		}
	}

	return false;
}

bool augmentFre(int id) {
	if (knownFrench[id] || visitedFre[id]) return false;
	visitedFre[id] = true;

	if (matchedFre[id] >= 0) return augmentEng(matchedFre[id]);
	else return true;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;

		words = 0;
		wordid.clear();

		for (int i = 0; i < 5000; i++) {
			knownEnglish[i] = knownFrench[i] = false;
			commonLang[i].clear();
			matchedEng[i] = matchedFre[i] = -1;
		}

		string s;
		getline(cin, s);

		int totalKnown = 0;
		for (int i = 0; i < N; i++) {
			getline(cin, s);

			vector<int> words;

			istringstream istr(s);
			string w;
			while (istr >> w) {
				int id = getID(w);
				if (i == 0 && !knownEnglish[id]) {
					knownEnglish[id] = true;
					totalKnown++;
				}
				if (i == 1 && !knownFrench[id]) {
					knownFrench[id] = true;
					totalKnown++;
				}
				words.push_back(id);
			}

			for (int id : words) {
				for (int id2 : words) {
					commonLang[id].push_back(id2);
				}
			}
		}

		bool cont = true;
		int matched = 0;
		while (cont) {
			cont = false;

			for (int j = 0; j < words; j++) visitedEng[j] = visitedFre[j] = false;
			for (int j = 0; j < words; j++) if (matchedEng[j] < 0 && augmentEng(j)) {
				matched++;
				cont = true;
			}
		}

		cout << "Case #" << t << ": " << (totalKnown+matched-words) << '\n';
	}

	return 0;
}

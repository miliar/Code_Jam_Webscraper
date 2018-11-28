#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

#define loop(i, n) for (int i = 0; i < n; i++)

const int MAX_WORDS = 2 * 1000 + 20 * 10;
vector<string> all_words;
vector< vector<string> > input_words;
vector< vector<int> > input_ids;
int is_english[MAX_WORDS];
int is_french[MAX_WORDS];

void read_words(vector<string> &v) {
	string line;
	getline(cin, line);
	istringstream ss(line);
	v.clear();
	string s;
	while (ss >> s) {
		v.push_back(s);
		all_words.push_back(s);
	}
}

int lookup(string &name) {
	return lower_bound(all_words.begin(), all_words.end(), name) - all_words.begin();
}

void mark(vector<int> &ids, int *lang) {
	loop(i, ids.size()) {
		lang[ids[i]]++;
	}
}

void unmark(vector<int> &ids, int *lang) {
	loop(i, ids.size()) {
		lang[ids[i]]--;
	}
}

int count_bi() {
	int count = 0;
	loop(i, all_words.size()) {
		if (is_english[i] && is_french[i]) {
			count++;
		}
	}
	return count;
}

int solve(int i) {
	if (i == input_ids.size()) {
		return count_bi();
	}
	mark(input_ids[i], is_english);
	int v1 = solve(i+1);
	unmark(input_ids[i], is_english);
	mark(input_ids[i], is_french);
	int v2 = solve(i+1);
	unmark(input_ids[i], is_french);
	return min(v1, v2);
}

int main() {
	int T, N;
	cin >> T;
	loop(t, T) {
		all_words.clear();
		cin >> N;
		string dump;
		getline(cin, dump);
		input_words.resize(N);
		input_ids.resize(N);
		loop(i, N) {
			read_words(input_words[i]);
		}
		sort(all_words.begin(), all_words.end());
		all_words.erase(unique(all_words.begin(), all_words.end()),
				all_words.end());
		loop(i, all_words.size()) {
			is_french[i] = is_english[i] = 0;
		}
		loop(i, N) {
			input_ids[i].clear();
			loop(j, input_words[i].size()) {
				input_ids[i].push_back(lookup(input_words[i][j]));
			}
		}
		mark(input_ids[0], is_english);
		mark(input_ids[1], is_french);
		cout << "Case #" << (t+1) << ": " << solve(2) << "\n";
	}
}

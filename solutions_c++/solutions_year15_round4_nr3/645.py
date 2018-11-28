#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <unordered_map>
#include <unordered_set>

using namespace std;

template <class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cerr << "Case #" << caseNumber << endl;
	cout << "Case #" << caseNumber << ": " << ans << endl;
}

int SolveTestCase() {
    int n;
    cin >> n;
    vector< vector<int> > sent(n);
    string tmp;
    map<string, int> words;
    getline(cin, tmp);
    int numWords = 0;
    for (int i = 0; i < n; i++) {
        getline(cin, tmp);
        istringstream iss(tmp);
        string word;
        while (iss >> word) {
            if (words.find(word) == words.end()) {
                words[word] = numWords;
                numWords++;
            }
            sent[i].push_back(words[word]);
        }
    }

    int ans = 1 << 30;
    int len = (1 << n);
    for (int i = 1; i < len; i += 4) {
        vector<bool> english(numWords);

        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                for (int s : sent[j]) {
                    english[s] = true;
                }
            }
        }
        vector<bool> both(numWords);
        for (int j = 0; j < n; j++) {
            if ( (i & (1 << j)) == 0) {
                for (const auto& s : sent[j]) {
                    if (english[s]) {
                        both[s] = true;
                    }
                }
            }
        }
        int cur = 0;
        for (auto b : both) {
            cur += b;
        }
        ans = min(ans, cur);
    }

    return ans;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("small.in", "r", stdin);
	//freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase() );

	return 0;
}
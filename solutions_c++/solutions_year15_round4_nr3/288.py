#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <functional>
#include <cstdint>
#include <cmath>
#include <unordered_set>
#include <unordered_map>
#include <sstream>

#define D(x) x

using namespace std;

void read_to_newline(istream& is) {
    string line;
    getline(cin, line);
}

void read_sentence(istream& is, vector<string>& words) {
    string line;
    getline(cin, line);

    istringstream iss(line);
    string word;
    while (true) {
        if (!(iss >> word)) break;
        words.push_back(word);
    }
}

int make_index(const string& word, map<string,int>& dict) {
    map<string,int>::iterator it = dict.find(word);
    int index;
    if (it == dict.end()) {
        index = dict.size();
        dict[word] = index;
    } else {
        index = it->second;
    }
    return index;
}

int main() {
    int numCases;
    cin >> numCases;

    for (int testCase = 1; testCase <= numCases; testCase++) {
        map<string,int> dict;

        int N;
        cin >> N;
        read_to_newline(cin);

        vector<vector<int>> sentences(N);
        for (int i = 0; i < N; i++) {
            vector<string> sentence;
            read_sentence(cin, sentence);
            for (string& word : sentence) {
                sentences[i].push_back(make_index(word, dict));
            }
        }

        int W = dict.size();
        vector<bool> english(W), french(W);
        for (int x : sentences[0]) {
            english[x] = true;
        }
        for (int x : sentences[1]) {
            french[x] = true;
        }

        int best = W;
        for (int mask = 0; mask < (1<<(N-2)); mask++) {
            vector<bool> current_english = english, current_french = french;
            for (int i = 2; i < N; i++) {
                bool is_french = (mask & (1<<(i-2))) != 0;

                for (int x : sentences[i]) {
                    if (is_french) {
                        current_french[x] = true;
                    } else {
                        current_english[x] = true;
                    }
                }
            }
            int current = 0;
            for (int i = 0; i < W; i++) {
                if (current_french[i] && current_english[i]) {
                    current++;
                }
            }
            best = min(best, current);
        }

        cout << "Case #" << testCase << ": " << best << endl;
    }
}

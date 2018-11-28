#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <utility>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>

using namespace std;

typedef long long LL;
template<class T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template<class T> inline T Sqr(const T& x) { return x * x; }



vector<string> Parse(const string& s) {
    istringstream ins(s);
    vector<string> words;
    string word;
    while (ins >> word) {
        words.push_back(word);
    }
    return words;
}


void AddToDict(map<string, int>& dict, string word) {
    auto it = dict.find(word);
    if (it == dict.end()) {
        int sz = dict.size();
        dict[word] = sz;
    }
}


void Solution() {
    int n;
    cin >> n;
    string line;
    getline(cin, line);
    map<string, int> dict;
    vector<vector<string>> sentsTmp;
    for (int i = 0; i < n; ++i) {
        getline(cin, line);
        vector<string> words = Parse(line);
        for (size_t j = 0; j < words.size(); ++j) {
            AddToDict(dict, words[j]);
        }
        sentsTmp.push_back(words);
    }
    int m = dict.size();
    vector<vector<int>> sents;
    for (int i = 0; i < n; ++i) {
        vector<int> sent;
        for (int j = 0; j < sentsTmp[i].size(); ++j) {
            sent.push_back(dict[sentsTmp[i][j]]);
        }
        sents.push_back(sent);
    }

    if (n == 2) {
        set<int> different;
        for (int i = 0; i < sents[0].size(); ++i) {
            bool found = false;
            for (int j = 0; j < sents[1].size(); ++j) {
                if (sents[0][i] == sents[1][j]) {
                    found = true;
                    break;
                }
            }
            if (found) {
                different.insert(sents[0][i]);
            }
        }
        cout << different.size() << endl;
        return;
    }


    int mn = -1;
    for (int mask = 0; mask < (1<<(n-2)); ++mask) {
        vector<int> isE(m);
        vector<int> isF(m);
        for (int i = 0; i < sents[0].size(); ++i) {
            isE[sents[0][i]] = 1;
        }
        for (int i = 0; i < sents[1].size(); ++i) {
            isF[sents[1][i]] = 1;
        }
        for (int i = 0; i < n - 2; ++i) {
            if (mask & (1<<i)) {
                for (int j = 0; j < sents[i + 2].size(); ++j) {
                    isE[sents[i + 2][j]] = 1;
                }
            } else {
                for (int j = 0; j < sents[i + 2].size(); ++j) {
                    isF[sents[i + 2][j]] = 1;
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i < m; ++i) {
            if (isE[i] && isF[i]) {
                ++cnt;
            }
        }
        if (mn == -1 || mn > cnt) {
            mn = cnt;
        }
    }
    cout << mn << endl;
}


int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        float startTime = clock() / CLOCKS_PER_SEC;
        cout << "Case #" << i + 1 << ": ";
        Solution();
        float endTime = clock() / CLOCKS_PER_SEC;
        cerr << "Test #" << i + 1 << ": elapsed time is " << endTime - startTime;
        cerr << endl;
    }

    return 0;
}



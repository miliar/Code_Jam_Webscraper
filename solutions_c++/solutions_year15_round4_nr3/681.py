#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <set>
#include <unordered_map>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

//const char* inputFile = "file.in";
//const char* outputFile = "file.out";
const char* inputFile = "C-small-attempt1.in";
const char* outputFile = "C-small-attempt1.out";
//const char* inputFile = "C-large-practice.in";
//const char* outputFile = "C-large-practice.out";

const int INF = 1e9;

class Solver {
public:
    Solver() {
    }

    vector<string> readSentence() {
        string str;
        getline(cin, str);
        stringstream ss(str);
        string s;
        vector<string> result;
        while (ss >> s) {
            result.push_back(s);
        }
        return result;
    }

    void addWords(const vector<string>& src, set<string>& dst) {
        for (const auto& word : src) {
            dst.insert(word);
        }
    }

    int findIntersect(const set<string>& lhs, const set<string>& rhs) const {
        int ans = 0;
        for (const auto& word : lhs) {
            if (rhs.find(word) != rhs.end()) {
                ans++;
            }
        }
        return ans;
    }

    int curAns = 0;

    void addEnglish(const vector<string>& words) {
        for (const auto& word : words) {
            int can = ++canEnglish[word];
            if (can == 1) {
                if (canFrench[word]) {
                    curAns += 1;
                }
            }
        }
    }

    void decEnglish(const vector<string>& words) {
        for (const auto& word : words) {
            int can = --canEnglish[word];
            if (can == 0) {
                if (canFrench[word]) {
                    curAns -= 1;
                }
            }
        }
    }

    void addFrench(const vector<string>& words) {
        for (const auto& word : words) {
            int can = ++canFrench[word];
            if (can == 1) {
                if (canEnglish[word]) {
                    curAns += 1;
                }
            }
        }
    }

    void decFrench(const vector<string>& words) {
        for (const auto& word : words) {
            int can = --canFrench[word];
            if (can == 0) {
                if (canEnglish[word]) {
                    curAns -= 1;
                }
            }
        }
    }

    string solveTest() {
        cin >> N;
        char c[1];
        gets(c);
        english = readSentence();
        french = readSentence();
        sentences.resize(N);
        for (int i = 0; i < N - 2; ++i) {
            sentences[i] = readSentence();
        }
        int maxMask = (1LL << (N - 2));
        int minIntersect = 1e9;
        addEnglish(english);
        addFrench(french);
        for (int mask = 0; mask < maxMask; ++mask) {
            int pow2 = 1;
            for (int bit = 0; bit < N - 2; ++bit) {
                if (mask & pow2) {
                    addFrench(sentences[bit]);
                } else {
                    addEnglish(sentences[bit]);
                }
                pow2 *= 2;
            }
            int intesect = curAns;
            minIntersect = min(minIntersect, intesect);
            pow2 = 1;
            for (int bit = 0; bit < N - 2; ++bit) {
                if (mask & pow2) {
                    decFrench(sentences[bit]);
                } else {
                    decEnglish(sentences[bit]);
                }
                pow2 *= 2;
            }
        }
        return to_string(minIntersect);
    }

    unordered_map<string, int> canEnglish;
    unordered_map<string, int> canFrench;
    vector<string> english;
    vector<string> french;
    set<string> allEnglish;
    set<string> allFrench;
    vector<vector<string>> sentences;
    int N;
};

int main() {
    freopen(inputFile, "r", stdin);
    freopen(outputFile, "w", stdout);
    int T;
    scanf("%d", &T);

    for (int testNumber = 1; testNumber <= T; ++testNumber) {
        DB(testNumber);
        Solver solver;
        string verdict = solver.solveTest();
        printf("Case #%d: %s\n", testNumber, verdict.c_str());
    }
    return 0;
}

#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;
    string s;
    string res;

    vector<string> letters;
    letters.push_back("ZERO");
    letters.push_back("ONE");
    letters.push_back("TWO");
    letters.push_back("THREE");
    letters.push_back("FOUR");
    letters.push_back("FIVE");
    letters.push_back("SIX");
    letters.push_back("SEVEN");
    letters.push_back("EIGHT");
    letters.push_back("NINE");

    vector< vector<int> > l(letters.size(), vector<int>(26, 0));

    for (int i = 0; i < letters.size(); ++i) {
        for (int j = 0; j < letters[i].size(); ++j) {
            ++l[i][letters[i][j] - 'A'];
        }
    }

    for (int test_ind = 0; test_ind < t; ++test_ind) {
        cin >> s;
        res.clear();

        vector<int> sv(26, 0);
        for (int j = 0; j < s.size(); ++j) {
            ++sv[s[j] - 'A'];
        }

        int used_count = 0;
        vector<int> res_num;
#define USE(LETTER, NUM)                                               \
            if (sv[LETTER - 'A'] > 0) {                                \
                int start_count = sv[LETTER - 'A'];                    \
                for (int j = 0; j < start_count; ++j) {           \
                    res_num.push_back(NUM);                            \
                    used_count += letters[NUM].size();                 \
                    for (int k = 0; k < letters[NUM].size(); ++k) {    \
                        --sv[letters[NUM][k] - 'A'];                   \
                    }                                                  \
                }                                                      \
            }

            USE('Z', 0);
            USE('W', 2);
            USE('X', 6);
            USE('G', 8);
            USE('H', 3);
            USE('R', 4);
            USE('F', 5);
            USE('V', 7);
            USE('O', 1);
            USE('I', 9);
#undef USE
      //if (used_count < s.size()) {
      //    cerr << "something bad with s:" << s << endl;
      //}


        sort(res_num.begin(), res_num.end());
        for (int i = 0; i < res_num.size(); ++i) {
            res.push_back('0' + res_num[i]);
        }
        cout << "Case #" << test_ind + 1 << ": " << res << endl;
    }
}


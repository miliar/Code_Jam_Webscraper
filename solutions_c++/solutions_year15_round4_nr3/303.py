#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <iomanip>

using namespace std;

#define pb push_back
#define f first
#define s second
typedef long long ll;
typedef pair<int, int> pint;
typedef pair<long long, long long> plint;
typedef vector<int> vint;
typedef vector<vector<int>> vvint;
typedef vector<long long> vlint;
typedef vector<vector<long long>> vvlint;
typedef vector<pair<int, int>> vpint;
typedef vector<pair<long long, long long>> vplint;

ifstream in("C-small-attempt0.in");
ofstream out("C-small-attempt0.out");


void go(int i, int n, const vector<vector<int>> &sents, vector<int> &sent_marks, vector<vector<bool>> &marks, int &biling_count, int &min_biling_count) {
    if (i == n) {
        min_biling_count = min(min_biling_count, biling_count);
        return;
    }



    for (int m = 0; m <= 1; ++m) {
        sent_marks[i] = m;
        vector<int> new_biling_words;
        vector<int> new_lang_words;
        for (auto w : sents[i]) {
            if (!marks[w][m]) {
                if (marks[w][1 - m]) {
                    new_biling_words.pb(w);
                    new_lang_words.pb(w);
                } else {
                    new_lang_words.pb(w);
                }
                marks[w][m] = true;
            }
        }

        biling_count += new_biling_words.size();

        go(i + 1, n, sents, sent_marks, marks, biling_count, min_biling_count);

        biling_count -= new_biling_words.size();

        for (auto w : new_lang_words) {
            marks[w][m] = false;
        }
    }
}


void solve()
{
    int n;
    in >> n;
    map<string, int> dict;
    vector<vector<int>> sents(n);

    string tmp;
    getline(in, tmp);

    for (int i = 0; i < n; ++i) {
        string s;
        getline(in, s);
        string word;
        s.pb(' ');
        for (char c : s) {
            if (c == ' ') {
                auto it = dict.find(word);
                int num = 0;
                if (it == dict.end()) {
                    int size = dict.size();
                    dict[word] = num = size;
                } else {
                    num = it->second;
                }
                sents[i].pb(num);
                word.erase();
            } else {
                word.pb(c);
            }
        }
    }
    int word_count = dict.size();
    vector<vector<bool>> marks(word_count, vector<bool>(2, false));
    for (int i = 0; i <= 1; ++i) {
        for (auto w : sents[i]) {
            marks[w][i] = true;
        }
    }
    vector<int> sent_marks(n, 0);
    sent_marks[1] = 1;

    int biling_count = 0;
    int min_biling_count = 1e9;
    for (int w = 0; w < word_count; ++w) {
        biling_count += marks[w][0] * marks[w][1];
    }

    go(2, n, sents, sent_marks, marks, biling_count, min_biling_count);

    out << min_biling_count;
}

int main()
{
    int cases;
    in >> cases;
    for (int z = 0; z < cases; ++z) {
        out << "Case #" << z + 1 << ": ";
        solve();
        out << endl;
    }

    return 0;
}

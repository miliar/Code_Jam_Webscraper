#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <stack>
#include <assert.h>
#include <unordered_map>
#include <iomanip>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define mplus(x, y) ((x) == -1 || (y) == -1) ? -1 : ((x) + (y))
#define mmax(x, y) ((x) == -1 || (y) == -1) ? -1 : max((x), (y))
#define mmin(x, y) ((x) == -1) ? (y) : ((y) == -1) ? (x) : min((x), (y))
#define checkbit(n, k) (((1L << (k)) & (n)) != 0)

#define debug(x) cerr << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;


int64 f(vector<vector<string> > sentences) {
    int n = sentences.size();
    map<string, int> word_indexes;
    vector<vector<int> > isen(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < sentences[i].size(); ++j) {
            string word = sentences[i][j];
            map<string, int>::iterator it = word_indexes.find(word);
            int index;
            if (it == word_indexes.end()) {
                index = word_indexes.size();
                word_indexes[word] = index;
            } else {
                index = it->second;
            }
            isen[i].push_back(index);
        }
    }
    int l = word_indexes.size();
    int res = -1;
    for (int m = 1; m < (1L << n); m += 4) {
        vector<bool> is_english(l);
        vector<bool> is_french(l);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < isen[i].size(); ++j) {
                if (checkbit(m, i))
                    is_english[isen[i][j]] = true;
                else
                    is_french[isen[i][j]] = true;
            }
        }
        int r = 0;
        for (int i = 0; i < l; ++i) {
            assert(is_english[i] || is_french[i]);
            if (is_french[i] && is_english[i])
                ++r;
        }
        if (res == -1 || r < res)
            res = r;
    }
    return res;
}


vector<string> read_sentence() {
    string s;
    getline(cin, s);
    stringstream ss;
    ss << s;
    string word;
    vector<string> words;
    while (ss >> word) {
        words.push_back(word);
    }
    return words;
}


int main() {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        int n;
        cin >> n;
        string s;
        getline(cin, s);
        vector<vector<string> > sentences(n);
        for (int i = 0; i< n; ++ i) {
            sentences[i] = read_sentence();
        }
        int64 res = f(sentences);
        cout << "Case #" << tt << ": " << res << endl;
    }
}

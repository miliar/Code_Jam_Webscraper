#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef set<string> trie;
typedef vector<trie> config_t;

trie maketrie(const string &s) {
    trie ret;
    for (int i=0; i<=(int)s.size(); ++i) {
        ret.insert(s.substr(0, i));
    }
    return ret;
}

int numstr, numserv;
vector<trie> have;
map<config_t, int> ways;

void go(int at, config_t &cur, int anymask) {
    if (at == numstr) {
        if (anymask+1 == (1<<numserv)) {
            ++ways[cur];
        }
        return;
    }
    for (int i=0; i<numserv; ++i) {
        trie old = cur[i];
        for (auto s : have[at]) {
            cur[i].insert(s);
        }
        go(at+1, cur, anymask|(1<<i));
        cur[i] = old;
    }
}
void solve(int testcase) {
    cin >> numstr >> numserv;
    have.clear();
    for (int i=0; i<numstr; ++i) {
        string s;
        cin >> s;
        have.push_back(maketrie(s));
    }

    ways.clear();
    config_t cur(numserv);
    go(0, cur, 0);

    int maxsz = 0;
    int szways = 0;
    for (auto p : ways) {
        int cand = 0;
        for (int i=0; i<numserv; ++i) {
            cand += p.first[i].size();
        }
        if (cand > maxsz) {
            maxsz = cand;
            szways = p.second;
        } else if (cand == maxsz) {
            szways += p.second;
        }
    }
    cout << "Case #" << testcase << ": " << maxsz << ' ' << szways << '\n';
    cerr << "Case #" << testcase << ": " << maxsz << ' ' << szways << '\n';
}

int main() {
    int T;
    cin >> T;
    cerr << T << " cases total\n";
    for (int t=1; t<=T; ++t) {
        solve(t);
    }
	return 0;
}

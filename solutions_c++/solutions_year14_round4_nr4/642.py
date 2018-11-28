#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

void precalc () {

}

int trie(const vector<string>& v) {
    set<string> s;
    s.insert("");
    for (int i = 0; i < v.size(); ++i) {
        string cur = "";
        for (int j = 0; j < v[i].size(); ++j) {
            cur += v[i][j];
            s.insert(cur);
        }
    }
    return s.size();
}

int split(const vector<string>& v, const vector<int>& s) {
    vector< vector<string> > vs;
    for (int i = 0; i < v.size(); ++i) {
        if (s[i] >= vs.size()) vs.resize(s[i] + 1);
        vs[s[i]].push_back(v[i]);
    }

    int res = 0;
    for (int i = 0; i < vs.size(); ++i) {
        res += trie(vs[i]);
    }
    return res;
}

bool inc(vector<int>& s, int n) {
    s[0]++;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == n) {
            if (i + 1 == s.size()) return false;
            s[i + 1]++;
            s[i] = 0;
        }
    }
    return true;
}

bool isgood(const vector<int>& s, int n) {
    vector<int> cnt(n);
    for (int i = 0; i < s.size(); ++i) {
        cnt[s[i]]++;
    }

    for (int i = 0; i < n; ++i) {
        if (cnt[i] == 0) return false;
    }
    return true;
}

bool nxt(vector<int>& s, int n) {
    while(inc(s, n)) {
        if (isgood(s, n)) return true;
    }
    return false;
}

void solve () {
    int m, n;
    cin >> m >> n;

    vector<string> v(m);
    for (int i = 0; i < m; ++i) {
        cin >> v[i];
    }

    vector<int> s(m, 0);

    map<int, int> mp;
    if (isgood(s, n)) ++mp[split(v, s)];
    while(nxt(s, n)) {
        ++mp[split(v, s)];
    }
    cout << mp.rbegin()->first << " " << mp.rbegin()->second << endl;
}

int main() {
	freopen("D-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

    precalc();

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
        cerr << test << endl;
		cout << "Case #" << test << ": ";
        solve();
	}
	return 0;
}

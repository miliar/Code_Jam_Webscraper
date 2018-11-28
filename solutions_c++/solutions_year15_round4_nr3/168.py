#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <map>

using namespace std;

const int INF = 0x3fffffff;

int get_bit(int x, int pos) {
    return (x >> pos) & 1;
}

int mark(const vector<int> &s, int french, vector<bool> &e, vector<bool> &f) {
    int ret = 0;
    for (int i = 0; i < (int) s.size(); ++i) {
        if (french == 0) {
            if (f[s[i]] && !e[s[i]])
                ++ret;
            e[s[i]] = true;
        } else {
            if (e[s[i]] && !f[s[i]])
                ++ret;
            f[s[i]] = true;
        }
    }
    return ret;
}

vector<int> split(const string &s, map<string, int> &dict) {
    stringstream ss(s);
    string w;
    vector<int> ans;
    while (ss >> w) {
        if (dict.count(w) == 0) {
            int t = dict.size();
            dict[w] = t;
        }
        ans.push_back(dict[w]);
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs) {
        int n;
        cin >> n >> ws;

        vector< vector<int> > words(n);
        map<string, int> dict;
        for (int i = 0; i < n; ++i) {
            string s;
            getline(cin, s);
            words[i] = split(s, dict);
        }

        vector<bool> english(dict.size(), false), french(dict.size(), false);
        int base = 0;
        base += mark(words[0], 0, english, french);
        base += mark(words[1], 1, english, french);

        int ans = INF;
        for (int sset = 0; sset < (1 << (n - 2)); ++sset) {
            vector<bool> e = english, f = french;
            int curr = base;
            for (int i = 0; i < n - 2; ++i) {
                if (get_bit(sset, i))
                    curr += mark(words[i + 2], 0, e, f);
                else
                    curr += mark(words[i + 2], 1, e, f);
            }
            ans = min(ans, curr);
        }
        cout << "Case #" << cs << ": " << ans << endl;
    }
    return 0;
}

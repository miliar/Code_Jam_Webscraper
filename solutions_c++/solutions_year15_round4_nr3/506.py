#include <cstdio>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

struct trie {
    int to[26];
    int english;
    int french;
};

trie t[30000];
int tsize;

void init(int cur) {
    for (int i = 0; i < 26; i++) {
        t[cur].to[i] = -1;
    }
    t[cur].english = t[cur].french = 0;
}

int add(string &s) {
    int cur = 0;
    for (int i = 0; i < s.length(); i++) {
        char c = s[i] - 'a';
        if (t[cur].to[c] == -1) {
            init(tsize);
            t[cur].to[c] = tsize++;
        }
        cur = t[cur].to[c];
    }
    return cur;
}

void solve() {
    init(0);
    tsize = 1;
    
    int n;
    cin >> n;
    string s;
    getline(cin, s);
    
    vector<vector<int> > pos;
    
    for (int i = 0; i < n; i++) {
        getline(cin, s);
        vector<int> v;
        string temp = "";
        for (int j = 0; j <= s.length(); j++) {
            if (j == s.length() || s[j] < 'a' || s[j] > 'z') {
                if (temp != "") {
                    v.push_back(add(temp));
                }
                temp = "";
            }
            else {
                temp.push_back(s[j]);
            }
        }
        pos.push_back(v);
    }
    
    
    reverse(pos.begin(), pos.end());
    
    int initialcnt = 0;
    for (int j = 0; j < pos[n - 2].size(); j++) {
        int cur = pos[n - 2][j];
        t[cur].french++;
        if (t[cur].french == 1 && t[cur].english) {
            initialcnt++;
        }
    }
    for (int j = 0; j < pos[n - 1].size(); j++) {
        int cur = pos[n - 1][j];
        t[cur].english++;
        if (t[cur].english == 1 && t[cur].french) {
            initialcnt++;
        }
    }
    int mincnt = 3000;

    
    for (int mask = 0; mask < (1 << (n - 2)); mask++) {
        int curcnt = initialcnt;
        for (int i = 0; i < n - 2; i++) {
            int english = mask & (1 << i);
            for (int j = 0; j < pos[i].size(); j++) {
                int cur = pos[i][j];
                if (english) {
                    t[cur].english++;
                    if (t[cur].english == 1 && t[cur].french) {
                        curcnt++;
                    }
                }
                else {
                    t[cur].french++;
                    if (t[cur].french == 1 && t[cur].english) {
                        curcnt++;
                    }
                }
            }
        }
        for (int i = 0; i < n - 2; i++) {
            int english = mask & (1 << i);
            for (int j = 0; j < pos[i].size(); j++) {
                int cur = pos[i][j];
                if (english) {
                    t[cur].english--;
                }
                else {
                    t[cur].french--;
                }
            }
        }
        mincnt = min(mincnt, curcnt);
    }
    
    cout << mincnt;
}

int main(){
#ifndef ONLINE_JUDGE
    freopen("C-small-attempt1.in.txt", "rt", stdin);
//    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    
}

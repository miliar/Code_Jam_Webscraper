#include <bits/stdc++.h>
using namespace std;

typedef bitset<2200> bst;
vector<int> wids[200];
map<string, int> ids;
int maxid;
int n, ans;

void solve(int line, bst english, bst french) {
    if (line == n) {
        int common = 0;
        for (int i = 0; i < maxid; i++)
            if (english[i] and french[i])
                common++;
        if (ans > common)
            ans = common;
    } else {
        bst e1 = english, f1 = french;
        for (auto i: wids[line])
            e1.set(i);
        solve(line+1, e1, french);
        for (auto i: wids[line])
            f1.set(i);
        solve(line+1, english, f1);
    }
}

int main() {
    int cases;
    scanf("%d", &cases);
    for (int cs = 1; cs <= cases; cs++) {
        cin >> n;
        string line, word;
        getline(cin, line);
        ids.clear();
        maxid = 0;
        for (int i = 0; i < n; i++) {
            wids[i].clear();
            getline(cin, line);
            istringstream is(line);
            while (is >> word) {
                if (ids.count(word))
                    wids[i].push_back(ids[word]);
                else
                    wids[i].push_back(ids[word] = maxid++);
            }
            // for (auto s: wids[i]) cout << ' ' << s;
            // cout << endl;
        }
        ans = 1e8;
        bst english, french;
        for (auto i: wids[0])
            english.set(i);
        for (auto i: wids[1])
            french.set(i);
        solve(2, english, french);
        printf("Case #%d: %d\n", cs, ans);
    }
}

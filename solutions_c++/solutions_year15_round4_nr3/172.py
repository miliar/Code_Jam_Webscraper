#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

void solve() {
    int N;
    int it = 0;
    cin >> N;
    string line;
    getline(cin, line);
    map<string, int> words;
    vector<vector<int> > appearance;
    rep(i, N) {
        getline(cin, line);
        stringstream ss(line);
        string word;
        while (ss >> word) {
            if (words.find(word) == words.end()) {
                words[word] = it++;
                appearance.push_back(vector<int>());
            }
            appearance[words[word]].push_back(i);
        }
    }

    int ans = 1 << 29;
    for (int i = 0; i < (1 << N); i++) {
        int tmp = 0;
        if ((i & 1) != 0)continue;
        if ((i & 2) != 2) continue;
        //cerr << i << endl;
        rep(j, it) {
            int count = 0;
            rep(k, appearance[j].size()) {
                count += ((i >> appearance[j][k]) & 1) ? 1 : 0;
            }
            if (count != 0 && count != (int)appearance[j].size())tmp++;
            //cerr << tmp << endl;
        }
        ans = min(ans, tmp);
    }

    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": "; 
        solve();
    }
    return 0;
}

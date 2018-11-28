#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

int min_moves_bt(const map<int, int> &numb) {
    if (numb.size() == 1) return 0;
    map<int, int> ma1(numb), ma2(numb);
    int mo1, mo2;
    pair<int, int> p = *(ma1.begin());
    (++ma1.begin())->second += p.second;
    ma1.erase(ma1.begin());
    mo1 = p.second*(ma1.begin()->first - p.first);
    p = *(ma2.rbegin());
    (++ma2.rbegin())->second += p.second;
    ma2.erase(--ma2.end());
    mo2 = p.second*(p.first - ma2.rbegin()->first);
    //cerr << "mo1 mo2:" << mo1 << ' ' << mo2 << endl;
    return min(mo1 + min_moves_bt(ma1), mo2 + min_moves_bt(ma2));
}

int min_moves(vector<int> &numb) {
    map<int, int> mnum;
    for (int i = 0; i < numb.size(); ++i) ++mnum[numb[i]];
    return min_moves_bt(mnum);
}

int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas) {
        cout << "Case #" << cas << ": ";
        
        int N;
        cin >> N;
        vector<string> str(N);
        for (int i = 0; i < N; ++i) cin >> str[i];
        vector<int> ind(N, 0);
        bool possible = true;
        int moves = 0;
        while (ind[0] < str[0].size() and possible) {
            char c = str[0][ind[0]];
            vector<int> rep(N, 0);
            for (int i = 0; i < N and possible; ++i) {
                while (ind[i] < str[i].size() and str[i][ind[i]] == c) {
                   ++rep[i];
                   ++ind[i];
                }
                if (rep[i] == 0) possible = false;
            }
            moves += min_moves(rep);
        }
        for (int i = 1; i < N and possible; ++i) {
            if (ind[i] < str[i].size()) possible = false;
        }
        
        if (possible) cout << moves << endl;
        else cout << "Fegla Won" << endl;
    }
}

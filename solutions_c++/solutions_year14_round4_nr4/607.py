#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#define puba push_back

using namespace std;

int t, n, m;
vector <string> mas;
map <char, int> empty_map;

int num_v(vector <int> q) {
    vector <map <char, int> > trie;
    trie.puba(empty_map);
    for (int i = 0; i < (int) q.size(); ++i) {
        int now_pos = 0;
        for (int j = 0; j < (int) mas[q[i]].size(); ++j) {
            if (trie[now_pos][mas[q[i]][j]] == 0) {
                trie[now_pos][mas[q[i]][j]] = trie.size();
                trie.puba(empty_map);
            }
            now_pos = trie[now_pos][mas[q[i]][j]];
        }
    }
    return trie.size();
}

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> m >> n;
        mas.clear();
        string s;
        for (int j = 0; j < m; ++j) {
            cin >> s;   
            mas.puba(s);
        }
        int bs = pow(n, m);
        int max_ans = -1;
        int ans = 0;
        for (int j = 0; j < bs; ++j) {
            vector <int> r[n];
            int temp = j;
            for (int k = 0; k < m; ++k) {
                r[temp % n].puba(k);
                temp /= n;
            }
            bool flag = false;
            for (int k = 0; k < n; ++k) {
                if (!r[k].size()) {
                    flag = true;   
                }
            }
            if (flag) {
                continue;
            }
            int sum_num_v = 0;
            for (int k = 0; k < n; ++k) {
                sum_num_v += num_v(r[k]);
            }
            if (max_ans < sum_num_v) {
                max_ans = sum_num_v;
                ans = 0;
            }
            if (max_ans == sum_num_v) {
                ans++;
            }
        }
        cout << "Case #" << i + 1 << ": " << max_ans << " " << ans << endl;
    }

    return 0;
}
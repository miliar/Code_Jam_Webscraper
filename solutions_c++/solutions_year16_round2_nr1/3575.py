#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

struct Node{
    Node(vector<int> h, vector<int> d) : hash(h), digits(d) {}
    vector<int> hash;
    vector<int> digits;
};

int main()
{
    string d2s[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

    int T; string S;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> S;
        // bfs
        vector<int> hash(26, 0);
        for (char c : S) ++hash[c - 'A'];
        bool finish = false;

        queue<Node> q; q.push(Node(hash, vector<int>()));
        while (!q.empty()) {
            Node& state = q.front();
            int start = state.digits.empty() ? 0 : state.digits[state.digits.size() - 1];
            for (int i = start; i <= 9; ++i) {
                vector<int> tmp_hash = state.hash;
                bool ok = true;
                for (char c : d2s[i]) {
                    --tmp_hash[c - 'A']; if (tmp_hash[c - 'A'] < 0) { ok = false; break; }
                }
                if (!ok) continue;
                vector<int> tmp_digits = state.digits;
                tmp_digits.push_back(i);
                q.push(Node(tmp_hash, tmp_digits));
                // terminate
                finish = true;
                for (int k = 0; k < 26; ++k) {
                    if (tmp_hash[k] != 0) { finish = false; break; }
                }
                if (finish) {
                    cout << "Case #" << t << ": ";
                    for (int dd : tmp_digits) cout << dd;
                    cout << endl;
                    break;
                }
            }
            if (finish) break;
            q.pop();
        }
    }
    return 0;
}

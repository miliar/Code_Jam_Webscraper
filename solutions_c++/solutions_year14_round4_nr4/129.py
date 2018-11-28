#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

struct trie {
    map<char, trie> children;

    void insert(const string &s, int i) {
        if (i < s.size())
            children[s[i]].insert(s, i+1);
    }

    int size() {
        int cnt = 1;

        for (auto i : children) {
            cnt += i.second.size();
        }

        return cnt;
    }
};

void backtrack(vector<string> &s, int i, int n, vector<int> &assignment, int &max_nodes, int &max_count) {
    if (i == s.size()) {
        set<int> servers(assignment.begin(), assignment.end());

        if (servers.size() == n) {
            vector<trie> ts(n);

            for (int j = 0; j < assignment.size(); j++)
                ts[assignment[j]].insert(s[j], 0);

            int nodes = 0;

            for (auto &t : ts)
                nodes += t.size();

            if (nodes > max_nodes) {
                max_nodes = nodes;
                max_count = 1;
            } else if (nodes == max_nodes) {
                max_count++;
            }
        }
    } else {
        for (int j = 0; j < n; j++) {
            assignment[i] = j;
            backtrack(s, i+1, n, assignment, max_nodes, max_count);
        }
    }
}

int main() {
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n, m;
        cin >> m >> n;

        vector<string> s(m);

        for (int i = 0; i < m; i++)
            cin >> s[i];

        int max_nodes = 0, max_count = 0;

        vector<trie> v(n);
        vector<int> assignment(m);

        backtrack(s, 0, n, assignment, max_nodes, max_count);

        cout << "Case #" << tc << ": " << max_nodes << " " << max_count << '\n';
    }

    return 0;
}

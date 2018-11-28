#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <sstream>
#include <set>

using namespace std;

bool dfs(int node, int sink, vector<bool> &used, vector< vector<int> > &E) {
    if (used[node])
        return false;
    used[node] = true;
    for (auto it = E[node].begin(); it != E[node].end(); ++it) {
        auto x = *it;
        if (x == sink || dfs(x, sink, used, E)) {
            E[x].push_back(node);
            swap(E[node].back(), *it);
            E[node].pop_back();
            return true;
        }
    }
    return false;
}

int main() {
    int T; cin >> T;

    for (int test = 1; test <= T; ++test) {
        int N; cin >> N;
        string ss; getline(cin, ss);
        map<string, int> values;
        auto get = [&](string s) {
            if (values.count(s))
                return values[s];
            return (values[s] = values.size());
        };

        vector< set<int> > S(N);
        for (int i = 0; i < N; ++i) {
            string line; getline(cin, line);
            istringstream in(line);
            string aux;
            while (in >> aux)
                S[i].insert(get(aux));
        }

        int source = 0;
        int sink = 1;
        vector< vector<int> > E(2 * values.size() + N);
        for (int i = 0; i < int(values.size()); ++i) {
            E[2 * i + N].push_back(2 * i + N + 1);
        }

        for (auto &x : S[0]) {
            E[source].push_back(2 * x + N);
        }

        for (auto &y : S[1]) {
            E[2 * y + N + 1].push_back(sink);
        }

        for (int i = 2; i < N; ++i)
            for (auto &x : S[i]) {
                E[2 * x + N + 1].push_back(i);
                E[i].push_back(2 * x + N);
            }

        int flow = 0;
        vector<bool> used(E.size(), false);
        while (dfs(source, sink, used, E)) {
            ++flow;
            used = vector<bool>(E.size(), false);
        }

       cout << "Case #" << test << ": " << flow << "\n";
    }
}

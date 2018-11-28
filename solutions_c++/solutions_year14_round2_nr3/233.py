#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

int n;
vector< vector< char > > adj;
vector< string > zips;

string show(vector< int > &order) {
    string res = "";
    for (auto i : order) {
        res += zips[i];
    }
    return res;
}

bool check(vector< int > &order) {
    vector< int > prev;
    int v = order[0];
    for (int i = 1; i < order.size(); ++i) {
        int u = order[i];
        while (!prev.empty() && !adj[v][u]) {
            v = prev.back();
            prev.pop_back();
        }
        if (!adj[v][u]) {
            return false;
        }
        prev.push_back(v);
        v = u;
    }
    return true;
}

int main() {
    cout.setf(ios_base::fixed);
    cout.precision(7);
    int T;
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cout << "Case #" << ti << ": ";
        int m;
        cin >> n >> m;
        zips.resize(n);
        cin.ignore();
        for (auto &zip : zips) {
            getline(cin, zip);
        }
        adj.assign(n, vector< char >(n, false));
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            a -= 1;
            b -= 1;
            adj[a][b] = true;
            adj[b][a] = true;
        }
        vector< int > order(n);
        for (int i = 0; i < n; ++i) {
            order[i] = i;
        }
        string ans = "";
        do {
            if (check(order)) {
                string option = show(order);
                if (ans.empty() || option < ans) {
                    ans = option;
                }
            }
        } while (next_permutation(order.begin(), order.end()));
        cout << ans;
        cout << "\n";
    }
    return 0;
}

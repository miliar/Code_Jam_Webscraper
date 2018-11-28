
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <set>
#include <string>
#include <utility>
#include <vector>
#define MAXM 1001
#define INF (1 << 30)
#define MOD 1000000007

using namespace std;

int N, M;
string s[MAXM];

vector <int> a[MAXM];

int get_nodes_single(const vector <int> &b) {
    set <string> all;
    all.insert("");
    for (int i : b)
        for (int j = 0; j < s[i].size(); j++)
            all.insert(s[i].substr(0, j + 1));
    return all.size();
}

int get_nodes() {
    int nodes = 0;
    for (int i = 0; i < N; i++)
        nodes += get_nodes_single(a[i]);
    return nodes;
}

void solve() {
    cin >> M >> N;
    for (int i = 0; i < M; i++)
        cin >> s[i];

    // brute force O(N^M)
    int total = 1;
    for (int i = 0; i < M; i++)
        total *= N;

    int most_nodes = 0;
    long long cnt = 0;
    for (int mask = 0; mask < total; mask++) {
        for (int j = 0; j < N; j++)
            a[j].clear();

        int cur = mask;
        for (int i = 0; i < M; i++) {
            a[cur % N].push_back(i);
            cur /= N;
        }

        bool empty = false;
        for (int j = 0; j < N; j++)
            if (a[j].size() == 0) {
                empty = true;
                break;
            }
        if (empty)
            continue;

        int nodes = get_nodes();
        if (nodes > most_nodes)
            most_nodes = nodes, cnt = 0;
        if (nodes == most_nodes)
            cnt++;
    }
    cout << most_nodes << " " << cnt << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
}


#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <cstring>
#include <cstdio>

using namespace std;


int M, N;
string S[1000];
int assign[1000];

int max_node, max_count;

void check() {
    set<string> machine[100];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j <= S[i].length(); j++) {
            machine[assign[i]].insert(S[i].substr(0, j));
        }
    }
    int curr = 0;
    for (int i = 0; i < N; i++) {
        if (machine[i].size() == 0)
            return;
        curr += machine[i].size();
    }

    if (curr > max_node) {
        max_node = curr;
        max_count = 1;
    } else if (curr == max_node)
        max_count++;
}

void search(int p) {
    if (p == M) {
        check();
        return;
    }

    for (int i = 0; i < N; i++) {
        assign[p] = i;
        search(p + 1);
    }
}

void solve() {
    cin >> M >> N;
    for (int i = 0; i < M; i++) {
        cin >> S[i];
    }

    max_node = -1;
    search(0);

    cout << max_node << ' ' << max_count << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }

    return 0;
}

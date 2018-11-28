#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <bitset>
#include <iomanip>
#include <vector>

using namespace std;

int N;
bitset<25> e[25];
char lr[25];
char rl[25];
bitset<25> visited;

bool dfs(int i, int exR) {
    if (visited[i]) return false;
    visited[i] = true;
    for (int j = 0; j < N; ++j) if (j != exR && e[i].test(j)) {
        if (rl[j] == -1 || dfs(rl[j], exR)) {
            rl[j] = i;
            lr[i] = j;
            return true;
        }
    }
    return false;
}

bool perfect(int exL = -1, int exR = -1) {
    memset(lr, -1, sizeof(lr));
    memset(rl, -1, sizeof(rl));
    bool r = true;
    for (int i = 0; i < N; ++i) if (i != exL) {
        visited.reset();
        if (!dfs(i, exR)) {
            if (exL >= 0) return false;
            r = false;
        }
    }
    return r;
}

void tc() {
    cin >> N;
    for (int i = 0; i < N; ++i) {
        e[i].reset();
        for (int j = 0; j < N; ++j) {
            char c;
            cin >> skipws >> c;
            if (c == '1') e[i].set(j);
        }
    }

    int cost = 0;

    if (false) {
        bitset<25> ee;
        for (int i = 0; i < N; ++i) ee |= e[i];
        int j = 0;
        for (int i = 0; i < N; ++i) if (e[i] == 0) for (; j < N; ++j) if (!ee.test(j)) {
            ++cost;
            e[i].set(j);
            //cerr << "VERY INITIAL " << i << "-" << j << endl;
            ++j;
            break;
        }
    }
    while (!perfect()) {

        //cerr << "gotta do it " << endl;
        int wut[25];
        for (int j = 0; j < N; ++j) wut[j]  =j ;
        random_shuffle(wut, wut+N);
        for (int i = 0; i < N; ++i) if (lr[i] < 0) for (int j_ = 0, j = wut[j_]; j_ < N; j = wut[++j_]) if (rl[j] < 0) {
            lr[i] = j;
            rl[j] = i;
            ++cost;
            e[i].set(j);
            //cerr << "INITIAL " << i << "-" << j << endl;
            goto next;
        }
next:;
    }
    assert(perfect());

    bool changed = true;
    while (changed) {
        changed = false;
        for (int i = 0; i < N; ++i) for (int j = 0; j < N; ++j) if (!e[i].test(j) && perfect(i, j)) {
            ++cost;
            changed = true;
            e[i].set(j);
            //cerr << "FEAS(i,j) " << i << "-" << j << endl;
        }
    }

    static int cas = 1;
    cout << "Case #" << cas++ << ": " << cost << endl;
}

int main() {
    srand(time(0));
    int T;
    cin >> T;
    while (T--) tc();
}

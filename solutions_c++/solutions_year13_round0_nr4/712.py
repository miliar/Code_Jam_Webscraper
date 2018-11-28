#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;
typedef unsigned long long ull;

struct Chest {
    int type;
    vi keys;
};

map<ull, int> memo;

bool dfs(bool locks[], int n, int keys[], vector<Chest>& v, int nlog, int log[], bool opened[]) {
    bool solved = true;
    For(i, n) {
        if (locks[i]) {
            solved = false;
            break;
        }
    }

    if (solved) return true;

    ull a = 0;
    For(i, n) {
        a = (a << 1) | (locks[i] ? 0 : 1);
//        a = (a << 1) | (locks[i] ? 1 : 0);
    }
    if (memo[a]) return false;
    memo[a] = 1;

    bool opened_chest[n];
    For(i, n) opened_chest[i] = false;

    For(i, n) {
        if (locks[i] && keys[v[i].type] > 0) {
            // unlcok i-th chest
            locks[i] = false;
            keys[v[i].type]--;
            log[nlog] = i;

            For(j, v[i].keys.size()) {
                int key = v[i].keys[j];
                keys[key]++;
                opened_chest[key] = true;
            }

            if (dfs(locks, n, keys, v, nlog+1, log, opened_chest)) { // found answer
                solved = true;
                break;
            }

            // back
            locks[i] = true;
            keys[v[i].type]++;
            For(j, v[i].keys.size()) {
                int key = v[i].keys[j];
                keys[key]--;
//                opened_chest[key] = false;
            }
        }
    }

    if (!solved) {
        For(i, n) {
            if (opened_chest[i]) opened[i] = true;
        }
    }
    return solved;
}

void calc(int n, int keys[], vector<Chest>& v) {
    bool locks[n];
    For(i, n) locks[i] = true;
    int log[1000];
    bool opened[n];
    For(i, n) opened[i] = false;

    memo.clear();
    bool solved = dfs(locks, n, keys, v, 0, log, opened);
    if (solved) {
        For(i, n) printf(" %d", log[i] + 1);
        printf("\n");
    }
    else {
        puts(" IMPOSSIBLE");
    }
}

int main() {
    // keyは0ベースに変換する
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int k, n;
        scanf("%d %d", &k, &n);

        int keys[1000] = {};
        For(i, k) {
            int key;
            scanf("%d", &key);
            keys[key-1]++;
        }

        vector<Chest> chests;
        For(i, n) {
            Chest chest;

            int type, nkeys;
            scanf("%d %d", &type, &nkeys);

            chest.type = type - 1;
            For(j, nkeys) {
                int key;
                scanf("%d", &key);
                chest.keys.push_back(key-1);
            }

            chests.push_back(chest);
        }

        printf("Case #%d:", cc+1);
        calc(n, keys, chests);
    }
}

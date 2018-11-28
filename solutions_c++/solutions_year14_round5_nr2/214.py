//
// upanddown.cpp
//
// Siwakorn Srisakaokul - ping128
// Written on Saturday, 31 May 2014.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>
#include <string.h>

#include <assert.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PII2;

#define MAXN 105

int hp[MAXN];
int gold[MAXN];
int N, diana_damage, tower_damage;

int dp[205][205 * 100]; // cur monster, free turns

int maximize(int cur_monster, int free_turns) {
    int mm;
    if (free_turns > 205 * 100) free_turns = 205 * 100 - 1;
    if (dp[cur_monster][free_turns] != -1) {
        return dp[cur_monster][free_turns];
    }
    mm = free_turns;
    if (cur_monster == N) return 0;
    int ret = 0;
    // ok not kill
    ret = max(ret, maximize(cur_monster + 1, free_turns + (hp[cur_monster] + tower_damage - 1) / tower_damage));
    // ok I wanna kill
    if (free_turns == 0) {
        int num = (hp[cur_monster] - 1) / tower_damage;
        int temp = hp[cur_monster] - num * tower_damage;
        if (num) {
            free_turns = num;
            if (free_turns * diana_damage >= temp) {
                ret = max(ret, maximize(cur_monster + 1, free_turns - (temp + diana_damage - 1) / diana_damage)+ gold[cur_monster]);
            }
        }
    } else {
        int num = (hp[cur_monster] - 1) / tower_damage;
        int temp = hp[cur_monster] - num * tower_damage;
        free_turns += num;
        if (free_turns * diana_damage >= temp) {
            //            if (cur_monster == 0 && free_turns == 1) cout << "A" << free_turns - (temp + diana_damage - 1) / diana_damage + num << endl;
            ret = max(ret, maximize(cur_monster + 1, free_turns - (temp + diana_damage - 1) / diana_damage)+ gold[cur_monster]);
        }
    }
    return dp[cur_monster][mm] = ret;
}

void solve() {
    for (int i = 0; i < 205; i++) {
        for (int j = 0; j < 100 * 205; j++) {
            dp[i][j] = -1;
        }
    }
    cin >> diana_damage >> tower_damage >> N;
    for (int i = 0; i < N; i++) {
        cin >> hp[i] >> gold[i];
    }
    cout << maximize(0, 1) << endl;
}

int main() {
    int test;
    scanf("%d", &test);
    for (int tt = 0; tt < test; tt++) {
        printf("Case #%d: ", tt + 1);
        solve();
        //        if (tt == 1) break;
    }
    return 0;
}

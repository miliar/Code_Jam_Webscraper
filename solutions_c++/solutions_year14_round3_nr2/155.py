#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int N_MAX = 105, LEN_MAX = 105, LETTERS = 26, MOD = 1000000007;

int N;
char car[N_MAX][LEN_MAX];
vector<int> starts[LETTERS], endings[LETTERS], inner[LETTERS], all[LETTERS];
bool same_group[LETTERS][LETTERS];
bool impossible;

void parse(char *str, int index) {
    int len = strlen(str);
    bool all_same = true;

    for (int i = 0; i < len; i++) {
        if (str[i] != str[0])
            all_same = false;
    }

    if (all_same) {
        all[(int) str[0] - 'a'].push_back(index);
        return;
    }

    // Must start and end with different letters (since they're not all the same letter)
    if (str[0] == str[len - 1]) {
        impossible = true;
        return;
    }

    starts[(int) str[0] - 'a'].push_back(index);
    endings[(int) str[len - 1] - 'a'].push_back(index);
    int start = 0, end = len - 1;

    while (str[0] == str[start]) {
        start++;
    }

    while (str[len - 1] == str[end]) {
        end--;
    }

    if (start > end) {
        return;
    }

    for (int i = start; i <= end; i++) {
        if (str[i] != str[i - 1]) {
            inner[(int) str[i] - 'a'].push_back(index);
        }
    }
}

int factorial(int n) {
    int fact = 1;

    while (n > 0) {
        fact = (long long) fact * n % MOD;
        n--;
    }

    return fact;
}

bool cycle() {
    for (int k = 0; k < LETTERS; k++) {
        for (int i = 0; i < LETTERS; i++) {
            for (int j = 0; j < LETTERS; j++) {
                same_group[i][j] |= same_group[i][k] && same_group[k][j];
            }
        }
    }

    for (int i = 0; i < LETTERS; i++) {
        if (same_group[i][i]) {
            return true;
        }
    }

    return false;
}

void solve_case(int test_case) {
    for (int letter = 0; letter < LETTERS; letter++) {
        starts[letter].clear();
        endings[letter].clear();
        inner[letter].clear();
        all[letter].clear();
    }

    impossible = false;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%s", car[i]);
        parse(car[i], i);
    }

    for (int letter = 0; letter < LETTERS; letter++) {
        if (starts[letter].size() > 1 || endings[letter].size() > 1 || inner[letter].size() > 1) {
            impossible = true;
        }

        if (inner[letter].size() > 0 && starts[letter].size() + endings[letter].size() + all[letter].size() > 0) {
            impossible = true;
        }
    }

    if (impossible) {
        printf("Case #%d: %d\n", test_case, 0);
        return;
    }

    long long answer = 1;

    for (int letter = 0; letter < LETTERS; letter++) {
        answer = answer * factorial(all[letter].size()) % MOD;
    }

    vector<int> groups;

    for (int letter = 0; letter < LETTERS; letter++) {
        if (starts[letter].size() > 0 || endings[letter].size() > 0 || all[letter].size() > 0) {
            groups.push_back(letter);
        }
    }

    memset(same_group, false, sizeof(same_group));

    for (int i = 0; i < N; i++) {
        int x = (int) car[i][0] - 'a';
        int y = (int) car[i][strlen(car[i]) - 1] - 'a';

        if (x != y) {
            same_group[x][y] = true;
        }
    }

    if (cycle()) {
        answer = 0;
    }

    int different_groups = 0;

    for (int i = 0; i < (int) groups.size(); i++) {
        bool different = true;

        for (int j = 0; j < i; j++) {
            if (same_group[groups[i]][groups[j]] || same_group[groups[j]][groups[i]]) {
                different = false;
            }
        }

        if (different) {
            different_groups++;
        }
    }

    answer = answer * factorial(different_groups) % MOD;
    printf("Case #%d: %d\n", test_case, (int) answer);
}

int main() {
    int T; scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        solve_case(tc);
        fflush(stdout);
    }

    return 0;
}

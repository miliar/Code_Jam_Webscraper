#include <algorithm>
#include <bitset>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <list>
#include <numeric>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

size_t num[10][26];

const char *letters[10] = {
    "ZERO",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
    "SIX",
    "SEVEN",
    "EIGHT",
    "NINE"
};

size_t letter_cnt[10] = {4, 3, 3, 5, 4, 4, 3, 5, 5, 4};

void init() {
    for (auto &digit : num) {
        for (auto &count : digit) {
            count = 0;
        }
    }
    for (size_t i = 0; i < 10; ++i) {
        for (size_t j = 0; j < letter_cnt[i]; ++j) {
            ++num[i][letters[i][j] - 'A'];
        }
    }
}

char str[2001];
size_t cnt[26];
size_t total_cnt;

string result;

bool dfs(size_t current) {
    //printf("CURRENT = %zd\n", current);
    if (total_cnt == 0) {
        //printf("TOTAL = 0\n");
        return true;
    }
    if (current > 9) {
        //printf("CURRENT > 9\n");
        return false;
    }
    bool yes = true;
    for (size_t i = 0; i < 26; ++i) {
        if (num[current][i] > cnt[i]) {
            yes = false;
            break;
        }
    }
    //printf("HAS %zd: %d\n", current, yes);
    if (yes) {
        total_cnt -= letter_cnt[current];
        result.push_back('0' + current);
        for (size_t i = 0; i < 26; ++i) {
            cnt[i] -= num[current][i];
        }
        if (dfs(current)) {
            return true;
        }
        if (dfs(current + 1)) {
            return true;
        }
        total_cnt += letter_cnt[current];
        result.pop_back();
        for (size_t i = 0; i < 26; ++i) {
            cnt[i] += num[current][i];
        }
    }
    if (dfs(current + 1)) {
        return true;
    } else {
        return false;
    }
}

int main(int argc, const char *argv[]) {
    freopen("B_A.in", "r", stdin);
    freopen("B_A.out", "w", stdout);
    init();
    size_t t = 0;
    scanf("%zd", &t);
    for (size_t i = 1; i <= t; ++i) {
        printf("Case #%zd: ", i);
        scanf("%s", str);
        memset(cnt, 0, sizeof(cnt));
        total_cnt = 0;
        size_t len = strlen(str);
        for (size_t j = 0; j < len; ++j) {
            ++cnt[str[j] - 'A'];
            ++total_cnt;
        }
        result = "";
        dfs(0);
        printf("%s\n", result.c_str());
    }
    return EXIT_SUCCESS;
}
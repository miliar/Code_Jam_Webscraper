#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

char ss[1010];

struct Count{
    int lvl, cnt;

    Count() {
        lvl = cnt = 0;
    }

    bool operator < (const Count &A) const {
        return lvl < A.lvl;
    }

};

void solve(int caseN) {
    int s_max;
    scanf("%d %s", &s_max, ss);

    vector <int> cnt(1010, 0);
    for (int i = 0; i <= s_max; i++) {
        cnt[i] = ss[i] - '0';
    }

    vector<Count> all;
    for (int i = 0; i <= s_max; i++) {
        Count c;
        c.lvl = i;
        c.cnt = cnt[i];
        all.push_back(c);
    }
    sort(begin(all), end(all));
    int ans = 0, currentLevel = 0, currentPeople = 0;
    for (auto c : all) {
        if (c.lvl <= currentPeople) {
            currentPeople += c.cnt;
        } else {
            int dx = c.lvl - currentPeople;
            currentPeople += c.cnt + dx;
            ans += dx;
        }
        currentLevel++;
    }
    printf("Case #%d: %d\n", caseN, ans);



}

int main() {
    int T;
    scanf("%d\n", &T);
    for (int i = 1; i <= T; i++) {
        solve(i);
    }

    return 0;
}
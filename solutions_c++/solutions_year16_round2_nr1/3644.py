#include <cstdio>
#include <vector>
#define pb push_back
#include <algorithm>
using namespace std;

const int MXl = 2e3 + 5;

char s[MXl];
vector<int> ans;

bool dfs(int* cnt) {
    char c = 'A';
    if (cnt['Z'-c] > 0 && cnt['E'-c] > 0 && cnt['R'-c] > 0 && cnt['O'-c] > 0) {
        cnt['Z'-c]--, cnt['E'-c]--, cnt['R'-c]--, cnt['O'-c]--; ans.pb(0);
        if (!dfs(cnt)) {
            cnt['Z'-c]++, cnt['E'-c]++, cnt['R'-c]++, cnt['O'-c]++; ans.pop_back();
        }
    }
    if (cnt['O'-c] > 0 && cnt['N'-c] > 0 && cnt['E'-c] > 0) {
        cnt['O'-c]--, cnt['N'-c]--, cnt['E'-c]--; ans.pb(1);
        if (!dfs(cnt)) {
            cnt['O'-c]++, cnt['N'-c]++, cnt['E'-c]++; ans.pop_back();
    
        }
    }
    if (cnt['T'-c] > 0 && cnt['W'-c] > 0 && cnt['O'-c] > 0) {
        cnt['T'-c]--, cnt['W'-c]--, cnt['O'-c]--; ans.pb(2);
        if (!dfs(cnt)) {
            cnt['T'-c]++, cnt['W'-c]++, cnt['O'-c]++; ans.pop_back();
        }
    }
    if (cnt['T'-c] > 0 && cnt['H'-c] > 0 && cnt['R'-c] > 0 && cnt['E'-c] > 1) {
        cnt['T'-c]--, cnt['H'-c]--, cnt['R'-c]--, cnt['E'-c] -= 2; ans.pb(3);
        if (!dfs(cnt)) {
            cnt['T'-c]++, cnt['H'-c]++, cnt['R'-c]++, cnt['E'-c] += 2; ans.pop_back();
        }
    }
    if (cnt['F'-c] > 0 && cnt['O'-c] > 0 && cnt['U'-c] > 0 && cnt['R'-c] > 0) {
        cnt['F'-c]--, cnt['O'-c]--, cnt['U'-c]--, cnt['R'-c]--; ans.pb(4);
        if (!dfs(cnt)) {
            cnt['F'-c]++, cnt['O'-c]++, cnt['U'-c]++, cnt['R'-c]++; ans.pop_back();
        }
    }
    if (cnt['F'-c] > 0 && cnt['I'-c] > 0 && cnt['V'-c] > 0 && cnt['E'-c] > 0) {
        cnt['F'-c]--, cnt['I'-c]--, cnt['V'-c]--, cnt['E'-c]--; ans.pb(5);
        if (!dfs(cnt)) {
            cnt['F'-c]++, cnt['I'-c]++, cnt['V'-c]++, cnt['E'-c]++; ans.pop_back();
        }
    }
    if (cnt['S'-c] > 0 && cnt['I'-c] > 0 && cnt['X'-c] > 0) {
        cnt['S'-c]--, cnt['I'-c]--, cnt['X'-c]--; ans.pb(6);
        if (!dfs(cnt)) {
            cnt['S'-c]++, cnt['I'-c]++, cnt['X'-c]++; ans.pop_back();
        }
    }
    if (cnt['S'-c] > 0 && cnt['E'-c] > 1 && cnt['V'-c] > 0 && cnt['N'-c] > 0) {
        cnt['S'-c]--, cnt['E'-c] -= 2, cnt['V'-c]--, cnt['N'-c]--; ans.pb(7);
        if (!dfs(cnt)) {
            cnt['S'-c]++, cnt['E'-c] += 2, cnt['V'-c]++, cnt['N'-c]++; ans.pop_back();
        }
    }
    if (cnt['E'-c] > 0 && cnt['I'-c] > 0 && cnt['G'-c] > 0 && cnt['H'-c] > 0 && cnt['T'-c] > 0) {
        cnt['E'-c]--, cnt['I'-c]--, cnt['G'-c]--, cnt['H'-c]--, cnt['T'-c]--; ans.pb(8);
        if (!dfs(cnt)) {
            cnt['E'-c]++, cnt['I'-c]++, cnt['G'-c]++, cnt['H'-c]++, cnt['T'-c]++; ans.pop_back();
        }
    }
    if (cnt['N'-c] > 1 && cnt['I'-c] > 0 && cnt['E'-c] > 0) {
        cnt['N'-c] -= 2, cnt['I'-c]--, cnt['E'-c]--; ans.pb(9);
        if (!dfs(cnt)) {
            cnt['N'-c] += 2, cnt['I'-c]++, cnt['E'-c]++; ans.pop_back();
        }
    }
    
    for (int i = 0; i < 30; i++)
        if (cnt[i] > 0) return false;
    return true;
}

int main(void) {
    freopen("A.small.in", "r", stdin);
    freopen("A.small.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int cnt[30];
        fill(cnt, cnt+30, 0);
        scanf("%s", s);
        for (int i = 0; s[i]; i++) cnt[s[i]-'A']++;
        
        ans.clear();
        dfs(cnt);
        printf("Case #%d: ", t);
        for (int i : ans) printf("%d", i);
        puts("");
    }
    return 0;
}
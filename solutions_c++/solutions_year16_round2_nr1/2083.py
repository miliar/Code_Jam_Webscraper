#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
string s;
string rf = "WXZUGORFSI";
int r[10] = { 2, 6, 0, 4, 8, 1, 3, 5, 7, 9 };
string d[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

int N;
int main() {
    scanf("%d", &N);
    for ( int t = 1; t <= N; t++ ) {
        vector<int> ans;
        cin >> s;
        int cnt[128];
        memset(cnt, 0, sizeof(cnt));
        for ( int i = 0; i < s.size(); i++ ) {
            cnt[s[i]]++;
        }
        for ( int i = 0; i < rf.size(); i++ ) {
            char c = rf[i];
            while ( cnt[c] > 0 ) {
                for ( int j = 0; j < d[r[i]].size(); j++ ) cnt[d[r[i]][j]]--;
                ans.push_back(r[i]);
            }
        }
        sort(ans.begin(), ans.end());
        printf("Case #%d: ", t);
        for ( int i = 0; i < ans.size(); i++ ) printf("%d", ans[i]);
        putchar('\n');
    }
    return 0;
}

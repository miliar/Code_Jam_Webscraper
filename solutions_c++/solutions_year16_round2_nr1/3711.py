#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define _ << " " <<
#define trace(x) cout << "# " << x << endl

using namespace std;

string numbers[10] = {"ZERO", "ONE", "TWO", "THREE",
                      "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

//int cnt[28];

vector<int> ans;

bool backtrack(int K, int cnt[28]) {
    if (K == 0) {
        int can = 1;
        for (int i = 0; i < 28; i++) if (cnt[i] != 0) can = 0;
        if (can) return true;
    }
    for (int i = 0; i < 10; i++) {
        string lookup = numbers[i];
        bool can = true;
        for (int j = 0; j < lookup.size(); j++) {
            if (cnt[lookup[j] - 'A'] == 0) can = false;
        }
        if (can) {
            ans.push_back(i);
            int much = 0;
            for (int j = 0; j < lookup.size(); j++) {
                cnt[lookup[j] - 'A']--;
                much++;
            }
            if (backtrack(K - much, cnt)) {
                return true;
            }
            ans.pop_back();
            for (int j = 0; j < lookup.size(); j++) {
                cnt[lookup[j] - 'A']++;
            }
        }
    }
    return false;
}

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for (int tt = 1; tt <= T; tt++) {
        ans.clear();
        string S;
        cin >> S;
        sort(S.begin(), S.end());
        int N = S.size();
        int K = 0;
        int cnt[28];
        memset(cnt, 0, sizeof(cnt));
        for (int i = 0; i < N; i++) {
            cnt[S[i] - 'A']++;
            K++;
        }
        backtrack(K, cnt);
        sort(ans.begin(), ans.end());
        cout << "Case #" << tt << ": ";
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i];
        }
        cout << endl;
    }
}

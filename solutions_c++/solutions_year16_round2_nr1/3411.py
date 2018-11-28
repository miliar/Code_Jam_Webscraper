/**
 * Author : Parachvte (ryannx6@gmail.com)
 * Date   : 04/30/2016
 */

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <utility>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define range(i, a, b) for (int i = (a), _end_ = (b); i <= _end_; ++i)
#define rep(i, n) for (int i = (0), _end_ = (n); i < _end_; ++i)
#define pb push_back
#define mp make_pair
#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

#define INF 1000000000
#define MOD 1000000007
#define EPS 1e-6

string num2str[10] = {
    "ZERO", // Z
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
string S;
int letter[26];
int use[10];

void dfs(int d) {
    if (d == 10) {
        for (int i = 'A'; i <= 'Z'; i++) {
            if (letter[i - 'A'] > 0) return;
        }
        for (int i = 0; i <= 9; i++)
            for (int j = 0; j < use[i]; j++)
                printf("%d", i);
        printf("\n");
        return;
    }

    int max_occur = INF;
    for (int i = 0, len = (int)num2str[d].length(); i < len; i++) {
        char ch = num2str[d][i];
        max_occur = min(max_occur, letter[ch - 'A']);
    }

    int min_occur = 0;
    if (d == 0) min_occur = max(min_occur, letter['Z' - 'A']);
    if (d == 2) min_occur = max(min_occur, letter['W' - 'A']);
    if (d == 6) min_occur = max(min_occur, letter['X' - 'A']);
    if (d == 8) min_occur = max(min_occur, letter['G' - 'A']);

    if (min_occur > max_occur) return;

    for (int o = min_occur; o <= max_occur; o++) {
        for (int i = 0, len = (int)num2str[d].length(); i < len; i++) {
            char ch = num2str[d][i];
            letter[ch - 'A'] -= o;
        }
        use[d] = o;
        dfs(d + 1);
        for (int i = 0, len = (int)num2str[d].length(); i < len; i++) {
            char ch = num2str[d][i];
            letter[ch - 'A'] += o;
        }
    }
}

void solve() {
    cin >> S;
    memset(letter, 0, sizeof(letter));
    for (int i = 0, len = (int)(S.length()); i < len; i++) {
        letter[S[i] - 'A'] += 1;
    }

    dfs(0);
}

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    std::ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}

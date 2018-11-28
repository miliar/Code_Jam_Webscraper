#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

#define MAXN 110
#define MAXL 110
#define INF 0x3f3f3f3f

int main() {
    int T, N;
    char str[MAXN][MAXL];
    vector< pair<char, int> > v[MAXN];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            scanf("%s", str[i]);
            v[i].clear();
        }

        for (int i = 0; i < N; i++) {
            int cnt = 1;
            int len = strlen(str[i]);
            for (int j = 1; j <= len; j++) {
                while (str[i][j] == str[i][j-1])
                    j++, cnt++;
                v[i].push_back(make_pair(str[i][j-1], cnt));
                cnt = 1;
            }
        }

        bool ok = 1;
        vector< pair<int, int> > range;
        for (int i = 0; i < v[0].size(); i++)
            range.push_back(make_pair(v[0][i].second, v[0][i].second));
        for (int i = 1; i < N; i++) {
            if (v[i].size() != range.size()) {
                ok = 0;
                break;
            }
            for (int j = 0; j < range.size(); j++) {
                if (v[i][j].first != v[0][j].first) {
                    ok = 0;
                    break;
                }
                range[j].first = min(range[j].first, v[i][j].second);
                range[j].second = max(range[j].second, v[i][j].second);
            }
        }

        printf("Case #%d: ", t);
        if (!ok) {
            puts("Fegla Won");
            continue;
        }

        int ans = 0;
        for (int i = 0; i < range.size(); i++) {
            int best = INF;
            for (int j = range[i].first; j <= range[i].second; j++) {
                int sum = 0;
                for (int k = 0; k < N; k++)
                    sum += abs(v[k][i].second - j);
                best = min(best, sum);
            }
            ans += best;
        }
        printf("%d\n", ans);
    }
}

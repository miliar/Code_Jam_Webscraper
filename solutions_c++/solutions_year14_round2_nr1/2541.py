#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>

using namespace std;

vector<pair<int, int> > v[100];

int pos(int x) {
    return x > 0 ?x :-x;
}

int main() {
    char in[110];
    int T, n;
    scanf("%d", &T);

    for (int times = 0; times < T; times++) {
        scanf("%d", &n);

        for (int i = 0; i < n; i++) {
            v[i] = vector<pair<int, int> >();
        }

        for (int i = 0; i < n; i++) {
            scanf("%s", in);
            int len = strlen(in);

            int t = in[0] - 'a';
            int cnt = 0;
            for (int j = 0; j < len; j++) {
                if (in[j] - 'a' == t) {
                    cnt++;
                }
                else {
                    v[i].push_back(pair<int, int>(t, cnt));
                    t = in[j] - 'a';
                    cnt = 1;
                }
            }
            v[i].push_back(pair<int, int>(t, cnt));
        }

        bool suc = true;
        for (int i = 0; i < n - 1; i++) {
            if (v[i].size() != v[i + 1].size()) {
                suc = false;
            }
            else {
                for (int j = 0; j < (int)v[i].size(); j++) {
                    if (v[i][j].first != v[i + 1][j].first) suc = false;
                }
            }
        }

        if (!suc) {
            printf("Case #%d: Fegla Won\n", times + 1);
        }
        else {
            int ans = 0;
            int s = v[0].size();
            for (int i = 0; i < s; i++) {
                double sum = 0;
                for (int j = 0; j < n; j++) {
                    sum += v[j][i].second;
                }

                sum /= n;
                double up = ceil(sum);
                double down = floor(sum);

                int su = 0;
                int sd = 0;
                for (int j = 0; j < n; j++) {
                    su += pos(v[j][i].second - up);
                    sd += pos(v[j][i].second - down);
                }
                ans += min(su, sd);
            }
            printf("Case #%d: %d\n", times + 1, ans);
        }
    }
}

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

typedef pair<int, int> PII;

bool b[257] = {0};
int T, n;
char s[1000005];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    b['a'] = b['e'] = b['i'] = b['o'] = b['u'] = 1;
    b[0] = 1;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "%d\n", test);
        vector<PII> v;
        scanf("%s%d", s, &n);
        int l = strlen(s);
        int now = -1;
        for (int i = 0; i <= l; ++i) {
            if (b[s[i]]) {
                if ((i - now > n) && (i)) {
                    v.push_back(make_pair(i - 1, now + 1));
                }
                now = i;
            }
        }
        long long ans = 0;
        for (int i = 0; i < l; ++i) {
            vector<PII>::iterator p = lower_bound(v.begin(), v.end(), make_pair(i, -10));
            if (p == v.end()) break;
            int tmp = -1;
            if (p->first - i + 1 < n) {
                if (++p == v.end()) break;
                tmp = p->second + n - 1;
            } else {
                tmp = max(p->second, i) + n - 1;
            }
            ans += l - tmp;
        }
        printf("Case #%d: %I64d\n", test, ans);
    }
    return 0;
}


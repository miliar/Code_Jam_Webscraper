#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
char ss[10005];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, s;
    scanf("%d", &t);
    for (int ca = 0; ca < t; ++ca) {
        scanf("%d%s", &s, ss);
        int sum = 0;
        int res = 0;
        //puts(ss);
        for (int level = 0; level <= s; ++level) {
            if (sum < level) {
                res = max(res, -(sum - level));
            }
            sum += ss[level] - '0';
        //while(1);
        }
        printf("Case #%d: %d\n", 1 + ca, res);
    }
}

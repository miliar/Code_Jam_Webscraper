#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
bool cmp(int a, int b) {
    return a > b;
}
int main(int argc, char *argv[])
{
    int disc[1000+50];
    int counter[1000+50];
    int t, n, x, s[1000+50];
    int ans = 0;
    scanf("%d", &t);
    for (int ct = 1; ct <= t; ct++) {
        printf("Case #%d: ", ct);
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; i++) {
            scanf("%d", &s[i]);
        }
        for (int i = 0; i < 1000+10; i++) {
            counter[i] = 0;
            disc[i] = 0;
        }
        ans = 0;
        sort(s, s+n, cmp);
        for (int i = 0; i < n; i++) {
            int j;
            for (j = 0; j <= ans; j++) {
                if (counter[j] < 2 && disc[j]+s[i] <= x) {
                    disc[j] += s[i];
                    counter[j]++;
                    break;
                }
            }
            if (j > ans) {
                ans++;
                disc[ans] = s[i];
                counter[j]++;
            }
        }
        printf("%d\n", ans+1);
    }
    return 0;
}

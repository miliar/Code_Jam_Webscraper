#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

void work() {
    int n;
    string s;
    cin >> n >> s;
    int ans = 0;
    int sum = 0;
    for (int i = 0; i <= n; i++) {
        if (sum < i) {
            ans += i - sum;
            sum = i;
        }
        sum += s[i] - '0';
    }
    printf("%d\n", ans);
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int T, C = 0;
    scanf("%d", &T);
    while (T--) {
        printf("Case #%d: ", ++C);
        work();
    }
    return 0;
}

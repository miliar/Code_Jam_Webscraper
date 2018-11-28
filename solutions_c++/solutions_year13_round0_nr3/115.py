#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 110;
int T, C;
long long dp[N][2][3][10], result[N];
char a[N], b[N];
int s[N];

long long solve(const char num[]) {
    int len = strlen(num);
    for (int i = 0; i < len; i++)
        s[i] = num[i] - '0';
    reverse(s, s + len);
    int n = (len + 1) / 2;
    memset(dp, 0, sizeof(dp));
    dp[0][0][0][0] = 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 3; k++)
                for (int l = 0; l < 10; l++)
                    if (dp[i][j][k][l] > 0) {
                        int st = (i == 0 ? 1 : 0);
                        int cur = dp[i][j][k][l];
                        int coef = (i + i + 2 > len ? 1 : 2);
                        for (int dig = st; dig * dig * coef + l <= 9; dig++) {
                            if (j == 0 && dig > s[len - i - 1]) continue;
                            int nj = (j == 0 ? (dig < s[len - i - 1]) : 1);
                            int nk = (dig == s[i] ? k : (dig < s[i] ? 1 : 2));
                            int nl = dig * dig * coef + l;
                            dp[i + 1][nj][nk][nl] += cur;
                        }
                    }
    long long ans = 0;
    for (int j = 0; j < 2; j++)
        for (int k = 0; k < 3; k++)
            if (j != 0 || k != 2)
                for (int l = 1; l < 10; l++)
                    ans += dp[n][j][k][l];
    return ans;
}
void init() {
    memset(a, 0, sizeof(a));
    memset(result, 0, sizeof(result));
    for (int i = 1; i <= 100; i++) {
        a[i - 1] = '9';
        result[i] = solve(a);
    }
    for (int i = 1; i <= 100; i++)
        result[i] += result[i - 1];
}

int sum[N], sqr[N], ret[N];
char* sqrt(char num[]) {
    memset(sum, 0, sizeof(sum));
    memset(sqr, 0, sizeof(sqr));
    memset(ret, 0, sizeof(ret));
    int len = strlen(num);
    for (int i = 0; i < len; i++)
        s[i] = num[i] - '0';
    reverse(s, s + len);
    int i, l = (len + 1) / 2;
    for (int p = l - 1; p >= 0; p--) {
        for (int dig = 0; dig < 9; dig++) {
            for (int i = 0; i <= len; i++)
                sum[i] = 0;
            for (int i = 0; i < len; i++) {
                sum[i] += sqr[i];
                sum[i + p] += 2 * ret[i];
            }
            sum[p + p]++;
            for (int i = 0; i < len; i++) {
                sum[i + 1] += sum[i] / 10;
                sum[i] %= 10;
            }
            int sum_len = len + 1;
            while (sum_len > 1 && sum[sum_len - 1] == 0)
                sum_len--;
            bool small = len < sum_len;
            if (!small)
                for (int i = len - 1; i >= 0; i--)
                    if (s[i] != sum[i]) {
                        small = s[i] < sum[i];
                        break;
                    }
            if (small) break;
            for (int i = 0; i < len; i++)
                sqr[i] = sum[i];
            ret[p] += 1;
        }
    }
    memset(num, 0, len + 1);
    for (int i = 0; i < l; i++)
        num[i] = ret[i] + '0';
    reverse(num, num + l);
    return num;
}
char* minus_one(char num[]) {
    int len = strlen(num);
    for (int i = len - 1; i >= 0; i--) {
        if (num[i] > '0') {
            num[i] -= 1;
            break;
        }
        num[i] = '9';
    }
    if (num[0] == '0' && len > 1)
        for (int i = 0; i < len; i++)
            num[i] = num[i + 1];
    return num;
}
int f(char num[]) {
    return solve(num) + result[strlen(num) - 1];
}
void run() {
    cin >> a >> b;
    long long ans = f(sqrt(b)) - f(sqrt(minus_one(a)));
    cout << "Case #" << C << ": " << ans << endl;
}

int main() {
    init();
    scanf("%d", &T);
    for (C = 1; C <= T; C++)
        run();
    return 0;
}

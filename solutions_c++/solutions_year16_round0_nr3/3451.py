#include<bits\stdc++.h>
using namespace std;
long long isPrime(long long n) {
    if (n == 2 || n == 3)
        return 0;
    if (n % 2 == 0)
        return 2;
    if (n % 3 == 0)
        return 3;
    long long limit = (int)floor(sqrt(n));
    for (long long i = 5, gap = 2; i <= limit; i += gap, gap = 6 - gap) 
        if (n % i == 0)
            return i;
    return 0;
}

void printBinary(long long n) {
    string s = "";
    while (n > 0) {
        s.push_back('0' + (n & 1));
        n >>= 1;
    }
    reverse(s.begin(), s.end());
    cout << s;
}

void solve(int N, int J) {
    long long ans = (1 << (N - 1)) + 1;
    while (ans <= (1 << N)) {
        bool ok = true;
        long long div[11] = { 0 };
        for (int i = 2; i <= 10; i++) {
            long long num = 0, tmp = 1, s = ans;
            while (s > 0) {
                if (s & 1)
                    num += tmp;
                tmp *= i;
                s >>= 1;
            }
            int ret = isPrime(num);
            if (ret == 0) {
                ok = false;
                break;
            }
            else {
                div[i] = ret;
            }
        }
        if (ok) {
            J--;
            printBinary(ans);
            for(int i = 2;i<=10;i++)
                printf(" %lld", div[i]);
            putchar('\n');
            if (J == 0)
                return;
        }
        ans += (1 << 1);
    }
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        int N, J;
        scanf("%d%d", &N, &J);
        printf("Case #%d:\n", c);
        solve(N, J);
    }
    return 0;
}
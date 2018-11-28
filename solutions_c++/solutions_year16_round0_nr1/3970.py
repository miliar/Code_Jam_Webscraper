#include<bits\stdc++.h>
using namespace std;
bool judge(bool digit[]) {
    for (int i = 0; i <= 9; i++)
        if (!digit[i])
            return false;
    return true;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int c = 1; c <= t; c++) {
        long long n, j = 1;
        scanf("%lld", &n);
        bool digit[10] = { false };
        while (!judge(digit)) {
            long long k = j * n;
            if (k == 0) 
                break;
            while (k > 0) {
                digit[k % 10] = true;
                k /= 10;
            }
            j++;
        }
        j--;
        if (!judge(digit))
            printf("Case #%d: INSOMNIA\n", c);
        else
            printf("Case #%d: %lld\n", c, n * j);
    }
    return 0;
}
#include <iostream>
using namespace std;

int digits(int n) {
    int digits = 0;
    while (n != 0) {
        digits |= 1 << (n % 10);
        n /= 10;
    }
    return digits;
}

int main() {
    int T, n;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d", &n);
        printf("Case #%d: ", t + 1);
        if (n == 0) {
            printf("INSOMNIA\n");
        } else {
            int num = n;
            int digs = digits(num);
            int multiplier = 2;
            while (digs != 0x3FF) {
                num = n * multiplier;
                multiplier++;
                digs |= digits(num);
            }
            printf("%d\n", num);
        }
    }
    return 0;
}

#include <stdio.h>
#include <algorithm>

using namespace std;

int get_digits(long long n) {
    int digits = 0;
    if (n == 0)
        return 1;
    while (n) {
        digits |= 1 << (n % 10);
        n /= 10;
    }
    return digits;
}

int main() {

    int T, digits;
    long long N, M;

    scanf("%d", &T);

    for (int ts = 0; ts < T; ts++) {

        scanf("%d\n", &N);

        printf("Case #%d: ", ts + 1);

        if (N == 0) {
            printf("INSOMNIA\n");
        }
        else {
            M = 0;
            digits = 0;
            while (digits != (1 << 10) - 1) {
                M += N;
                digits |= get_digits(M);
            }
            printf("%d\n", M);
        }
    }
}

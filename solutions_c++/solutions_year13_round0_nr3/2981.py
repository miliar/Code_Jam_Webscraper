#include <cstdio>

bool numbers[1000];

bool palyn(int n) {
    int number = n;
    int reverse = 0;
    while (number) {
        reverse *= 10;
        reverse += number % 10;
        number /= 10;
    }

    return (reverse == n);
}

void precalc() {
    for (int i = 0; i < 1000; i++) {
        numbers[i] = false;
    }
    for (int i = 0; i < 32; i++) {
        if (palyn(i) && palyn(i*i)) numbers[i*i] = true;
    }
}

int readandanswer() {
    int from, to;
    scanf("%d %d", &from, &to);

    int result = 0;
    for (int i = from; i <= to; i++) {
        if (numbers[i]) result++;
    }

    return result;
}

int main() {
    precalc();
//    for (int i = 0; i < 1000; i++) if (numbers[i]) printf("%d\n", i);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Case #%d: %d\n", i + 1, readandanswer());
    }
}

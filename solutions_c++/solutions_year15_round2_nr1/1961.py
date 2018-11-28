#include <cstdio>

int T;
int N;
int y;
int arr[1000005];
int reverse;

int rev (int n) {
    int reverse = 0;
    while (n > 9) {
        reverse += n % 10;
        n /= 10;
        reverse *= 10;
    }
    reverse += n;
    return reverse;
}

int main () {
    
    arr[1] = 1;
    for (int i = 1; i <= 1000000; i++) {
        if (arr[i + 1] == 0 || arr[i + 1] > arr[i] + 1) arr[i + 1] = arr[i] + 1;
        reverse = rev(i);
        if (reverse > i && (arr[reverse] == 0 || arr[reverse] > arr[i] + 1)) arr[reverse] = arr[i] + 1;
    }
    
    scanf("%d", &T);
    for (int x = 1; x <= T; x++) {
        scanf("%d", &N);
        y = arr[N];
        printf("Case #%d: %d\n", x, y);
    }
    
    return 0;
}
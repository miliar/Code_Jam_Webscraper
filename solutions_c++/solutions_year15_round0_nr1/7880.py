#include <cstdio>
int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int smax;
        unsigned char *arr;
        scanf(" %d ", &smax);
        arr = new unsigned char[smax+1];
        for (int s = 0; s < smax+1; s++) {
            arr[s] = getchar() - '0';
        }
        int sum = 0, inv = 0;
        for (int s = 0; s < smax+1; s++) {
            if (sum < s) {
                inv += s - sum;
                sum = s;
            }
            sum += arr[s];
        }
        delete[] arr;
        printf("Case #%d: %d\n", t, inv);
    }
    return 0;
}

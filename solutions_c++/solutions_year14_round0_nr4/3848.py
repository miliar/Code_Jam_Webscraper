#include <cstdio>
#include <cstdlib>
#include <algorithm>

int main() {
    int T, iter;
    FILE *in = fopen("input", "r"), *out = fopen("output", "w");
    int N;
    float n[1005], k0[1005], k1[1005];
    int i, index, j;
    float min;
    int r0, r1;
    fscanf(in, "%d", &T);
    for(iter = 0; iter < T; iter++) {
        fscanf(in, "%d", &N);
        for(i = 0; i < N; i++) {
            fscanf(in, "%f", n + i);
        }
        for(i = 0; i < N; i++) {
            fscanf(in, "%f", k0 + i);
        }
        std::sort(n, n + N);
        std::sort(k0, k0 + N);
        for(i = 0; i < N; i++) {
            k1[i] = k0[i];
        }
        std::reverse(k1, k1 + N);



        r1 = 0;
        for(i = 0; i < N; i++) {
            min = 10000.0;
            index = -1;
            for(j = 0; j < N; j++) {


                if(k0[j] > n[i] && k0[j] < min) {
                    index = j;
                    min = k0[j];
                }
            }
            if(min > 1.0) {
                r1++;
            }
            else {
                k0[index] = 0.0;
            }
        }
        std::reverse(n, n + N);
//        for(i = 0; i < N; i++) {
//            printf("data: %f %f\n", k1[i], n[i]);
//        }
        r0 = 0;
        for(i = 0; i < N; i++) {
            if(n[i] > k1[i]) {
                r0++;
            }
            else {
                for(j = N - 2; j >= i; j--) {
                    n[j + 1] = n[j];
                }
            }
        }
        fprintf(out, "Case #%d: %d %d\n", iter + 1, r0, r1);
    }
    fclose(in);
    fclose(out);
    return 0;
}

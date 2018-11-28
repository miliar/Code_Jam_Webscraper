#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
    FILE *in = fopen("B-small-attempt5.in", "r");
    FILE *out = fopen("B-small-out.out", "w");

    int T;
    fscanf(in, "%d", &T);

    int testCase;
    for (testCase = 1; testCase <= T; testCase++) {
        int A, B, K;
        fscanf(in, "%d %d %d", &A, &B, &K);

        int i, j, result = 0;
        for (i = 0; i < A; i++) {
            for (j = 0; j < B; j++) {
                if ((i & j) < K) {
                    result += 1;
                }
            }
        }

        fprintf(out, "Case #%d: %d\n", testCase, result);
    }

    fclose(in);
    fclose(out);
}
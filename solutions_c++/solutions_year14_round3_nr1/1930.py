#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int main(int argc, char *argv[]) {
    FILE *in = fopen("A-small-attempt0.in", "r");
    FILE *out = fopen("A-small.out", "w");

    int T;
    fscanf(in, "%d", &T);

    int testCase;
    for (testCase = 1; testCase <= T; testCase++) {
        long long a, b;
        fscanf(in, "%lld / %lld", &a, &b);

        long long i = 2, maxd = 1;
        while (i <= a) {
            if (a % i == 0 && b % i == 0) {
                maxd = i;
            }
            ++i;
        }

        a /= maxd;
        b /= maxd;

        int p = 0, im = 0;
        while (b > 1) {
            if (b % 2 != 0) {
                im = 1;
                break;
            }

            b /= 2;
            ++p;
        }

        if (im) {
            fprintf(out, "Case #%d: impossible\n", testCase);
            continue;
        }

        int m = 1, pm = 0;
        while (a >= m) {
            m *= 2;
            ++pm;
        }

        m /= 2;
        --pm;

        fprintf(out, "Case #%d: %d\n", testCase, p - pm);
    }

    fclose(in);
    fclose(out);
}
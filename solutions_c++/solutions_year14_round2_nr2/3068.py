#include <cstdio>
#include <string>

int main()
{
    FILE *in, *out;
    in = fopen("B-small-attempt1.in", "r");
    out = fopen("output", "w");
    int ITER_NUM, iter;
    long long unsigned i, j, k;
    long long unsigned r;
    long long unsigned ii, jj;
    fscanf(in, "%d", &ITER_NUM);
    for(iter = 0; iter < ITER_NUM; iter++) {
        fscanf(in, "%llu %llu %llu", &i, &j, &k);
        r = 0;//k * k + (i + j  - 2 * k) * k;
        for(ii = 0; ii < i; ii++)
            for(jj = 0; jj < j; jj++) {
                if((ii & jj) < k) r++;
        }
        fprintf(out, "Case #%d: %llu\n", iter + 1, r);
    }
    fclose(in);
    fclose(out);
    return 0;
}

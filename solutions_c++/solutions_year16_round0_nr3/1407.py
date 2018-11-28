#include <cstdio>
using namespace std;

int t, n, j;
long long divisor[9];

int main(void) {
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output.txt", "w");
    fscanf(input, "%d", &t);
    
    for (int tIter = 1; tIter <= t; tIter++) {
        fprintf(output, "Case #%d:\n", t);
        fscanf(input, "%d%d", &n, &j);
        
        for (int i = 0; i < 9; i++) {
            divisor[i] = 1;
            for (int k = 0; k < 16; k++)
                divisor[i] *= (i+2);
            divisor[i] += 1;
        }
        
        for (int i = 0; i < j; i++) {
            fprintf(output, "1");
            for (int k = 13; k >= 0; k--)
                fprintf(output, "%d", (i&(1<<k))?1:0);
            fprintf(output, "11");
            for (int k = 13; k >= 0; k--)
                fprintf(output, "%d", (i&(1<<k))?1:0);
            fprintf(output, "1");
            
            for (int k = 0; k < 9; k++)
                fprintf(output, " %lld", divisor[k]);
            fprintf(output, "\n");
        }
    }
    fclose(input);
    fclose(output);
    return 0;
}
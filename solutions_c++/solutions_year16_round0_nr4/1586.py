#include <cstdio>
using namespace std;

int t, k, c, s;

int main(void) {
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output.txt", "w");
    fscanf(input, "%d", &t);
    
    for (int tIter = 1; tIter <= t; tIter++) {
        fprintf(output, "Case #%d:", tIter);
        fscanf(input, "%d%d%d", &k, &c, &s);
        
        for (int i = 1; i <= k; i++)
            fprintf(output, " %d", i);
        fprintf(output, "\n");
    }
    fclose(input);
    fclose(output);
    return 0;
}
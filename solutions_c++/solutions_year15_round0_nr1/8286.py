// Example program
#include <stdio.h>
#include <string>

int main()
{
    int ncases;
    fscanf(stdin, "%d", &ncases);
    for (int t = 0; t < ncases; ++t) {
        int stotal;
        char S[1024];
        fscanf(stdin, "%d %s", &stotal, S);
        int acc = 0, missing = 0;
        for (int i = 0; i <= stotal; ++i) {
            int si = S[i] - '0';
            if (acc < i) {
                while(si == 0) {
                    i++;
                    si = S[i] - '0';
                }
                int delta = i - acc;
                missing += delta;
                acc += delta;
            }            
            acc += si;
        }
        fprintf(stdout, "Case #%d: %d\n", t+1, missing);
    }
}


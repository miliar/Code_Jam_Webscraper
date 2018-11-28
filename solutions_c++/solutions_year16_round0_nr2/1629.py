#include <cstdio>
#include <cstring>
using namespace std;

int t;
bool chk[101];
char cakes[101];

int main(void) {
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output.txt", "w");
    fscanf(input, "%d", &t);
    
    for (int tIter = 1; tIter <= t; tIter++) {
        fscanf(input, "%s", cakes);
        int len = strlen(cakes);
        for (int i = 0; i < len; i++)
            chk[i] = (cakes[i] == '-');
        chk[len] = false;
        
        int ans = 0;
        for (int i = 0; i < len; i++)
            if (chk[i] ^ chk[i+1])
                ans++;
                
        fprintf(output, "Case #%d: %d\n", tIter, ans);
    }
    fclose(input);
    fclose(output);
    return 0;
}
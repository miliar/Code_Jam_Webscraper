#include <cstdio>
using namespace std;

int t, n;
bool chk[10];

bool seenAllDigits() {
    for (int i = 0; i < 10; i++)
        if (!chk[i])
            return false;
    return true;
}

int main(void) {
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output.txt", "w");
    fscanf(input, "%d", &t);
    
    for (int tIter = 1; tIter <= t; tIter++) {
        fscanf(input, "%d", &n);
        if (n == 0) {
            fprintf(output, "Case #%d: INSOMNIA\n", tIter);
            continue;
        }
        for (int i = 0; i < 10; i++)
            chk[i] = false;
            
        int curr = 0;
        while (true) {
            curr += n;
            for (int i = curr; i > 0; i /= 10)
                chk[i%10] = true;
                
            if (seenAllDigits())
                break;
        }
        fprintf(output, "Case #%d: %d\n", tIter, curr);
    }
    fclose(input);
    fclose(output);
    return 0;
}
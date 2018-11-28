#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
using namespace std;

int main() {
    FILE* fout = fopen("B-large.out","w");
    FILE* fin = fopen("B-large.in", "r");
    int t;
    fscanf(fin, "%d", &t);
    int c = 0;
    while(t--) {
        c++;
        char str[200];
        int pancake[200];
        fscanf(fin, "%s", str);
        int len = strlen(str);
        for(int i = 0; i < len; i++) {
            if(str[i] == '+') pancake[i] = 1;
            else pancake[i] = 0;
        }
        int ans = 0;
        for(int i = len - 1; i >= 0; i--) {
            if(!pancake[i]) {
                ans++;
                pancake[i] = 1;
                for(int j = i - 1; j >= 0; j--) pancake[j] ^= 1;
            }
        }
        fprintf(fout, "Case #%d: %d\n", c, ans);
    }
    return 0;
}


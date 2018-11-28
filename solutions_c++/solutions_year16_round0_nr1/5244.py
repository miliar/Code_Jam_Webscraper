#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
using namespace std;

bool check(bool hash[10]) {
    for(int i = 0; i < 10; i++) if(!hash[i]) return false;
    return true;
}

void fillHash(bool hash[10], int n) {
    while(n) {
        hash[n%10] = true;
        n /= 10;
    }
}

int main() {
    FILE* fout = fopen("A-large.out","w");
    FILE* fin = fopen("A-large.in", "r");
    int t, n;
    fscanf(fin, "%d", &t);
    int c = 0;
    bool hash[10];
    while(t--) {
        c++;
        fscanf(fin, "%d", &n);
        memset(hash, 0, sizeof(hash));
        if(!n) {
            fprintf(fout, "Case #%d: INSOMNIA\n", c);
            continue;
        }
        int ans;
        for(int i = 1;;i++) {
            ans = n*i;
            fillHash(hash, ans);
            if(check(hash)) {
                fprintf(fout, "Case #%d: %d\n", c, ans);
                break;
            }    
        }
    }
    return 0;
}


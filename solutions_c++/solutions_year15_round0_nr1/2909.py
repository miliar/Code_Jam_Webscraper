#include <cstdio>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;
char s[1010];

int main(){
    FILE* FIN;
    FILE* FOUT;
    FIN = fopen("/Users/Djy/Documents/4test/A-large.in", "r");
    FOUT = fopen("/Users/Djy/Documents/4test/A-large.out", "w");
    
    int T;
    fscanf(FIN, "%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        fscanf(FIN, "%d%s", &n, s);
        int m = 0;
        for (int i = n; i >= 0; i--)
            if (s[i] > '0'){
                m = i;
                break;
            }
        int res = 0, now = 0;
        for (int i = 0; i <= m; i++)
        {
            if (now < i) res += i - now, now = i;
            now += s[i] - '0';
        }
        fprintf(FOUT, "Case #%d: %d\n", cas, res);
    }
    return 0;
}
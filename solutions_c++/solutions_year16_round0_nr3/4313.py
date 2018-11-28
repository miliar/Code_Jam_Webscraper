#include <bits/stdc++.h>

using namespace std;

int n, jj;

int main() {
    int T;
    scanf("%d", &T);
    scanf("%d%d", &n, &jj);
    
    printf("Case #1:\n");
    int cnt = 0;
    for(unsigned long long int i = (1llu << (n - 1)) + 1; i < (1llu << n); i += 2) {
        vector<long long> dv;
        for (int base = 2; base <= 10; ++base) {
            long long val = 0; 
            for (int j = n - 1; j >= 0; --j) {
                val = val * base + ((i >> j)&1);
            }
            for (long long int j = 2; j*j < val; ++j) {
                if (val % j == 0) {
                    dv.push_back(j);
                    break;
                }     
            } 
            if ((int)dv.size() < base - 1) {
                break;
            }
        }
        if (dv.size() == 9) {
            for (int j = n - 1; j >= 0; --j) {
                printf("%I64d", ((i >> j)&1));
            }
           
            for (int i = 0; i < 9; ++i) {
                printf(" %I64d", dv[i]);
            }
            ++cnt;
            printf("\n");
        }
        dv.resize(0);
        if (cnt == jj) break;
    }
}
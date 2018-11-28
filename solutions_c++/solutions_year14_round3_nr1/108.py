#include <iostream>
#include <stdio.h>

using namespace std;

long long T, P, Q;
char ls;
int caseNumber = 1;
long long gcd(long long x, long long y) {
    if (y == 0) return x;
    else return gcd(y, x % y);
}
int main() {
    freopen("elf.in", "r", stdin);    
    freopen("elf.out", "w", stdout);    
    cin >> T;
    while(T-- > 0) {
        scanf("%lld/%lld", &P, &Q);
        long long G = gcd(P, Q);
        P /= G;
        Q /= G;
        
        if ((Q & (Q - 1)) == 0LL) {
            int ret = 1;
            while(true) {
                long long Q2 = Q / 2;
                if (P >= Q2) {
                    break;
                } else {
                    Q = Q2;
                    ret++;
                }
            }
            printf("Case #%d: %d\n", caseNumber++, ret);
        } else {
            printf("Case #%d: impossible\n", caseNumber++);
        }
    }
    return 0;
}

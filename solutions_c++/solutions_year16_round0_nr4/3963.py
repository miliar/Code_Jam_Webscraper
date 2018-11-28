#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

long long t, k, c, s, pot;

int main() {
    scanf("%lld", &t);
    
    for (int i=1; i<=t; i++) {
        scanf("%lld %lld %lld", &k, &c, &s);
        
        pot = 1;
        for (int j=0; j<c; j++)
            pot *= k;

        printf("Case #%d: ", i);
        
        
        long long pot2 = pot/k;
        long long poz = 1;
        for (long long j=1; j<=k; j++) {
            printf("%lld ", poz);
            poz += pot2;
        }
        
        printf("\n");
    }
    
    return 0;
}

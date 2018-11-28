#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool v[11];

long long n, t;
int done;

void transform(long long x) {
    while (x > 0) {
        long long r = x % 10;
        if (v[r] == false)
            done++;
        v[r] = true;
        x /= 10;
    }
}

int main() {
    scanf("%lld", &t);
    
    for (int j=1; j<=t; j++) {
        for (int i=0; i<10; i++)
            v[i] = false;
        done = 0;
        scanf("%lld", &n);
        
        long long x = n;
        
        if (n == 0) {
            printf("Case #%d: INSOMNIA\n", j);
            continue;
        }
        
        while (done < 10) {
            transform(x);
            x += n;
        }
        x -= n;
        
        
        printf("Case #%d: %lld\n", j, x);
    }
    
    return 0;
}

#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

const int M = 1000005;
int ile = 0;

long long check(long long x) {
    long long a = 2;
    
    while (a * a <= x) {
        if (x % a == 0)
            return a;
        a++;
    }
    
    return -1;
}

void sprawdz(int x) {
    bool git = true;
    
    long long binary = 0;
    long long p = 1;
    
    while (x > 0) {
        long long r = x % 2;
        binary += (r * p);
        x /= 2;
        p *= 10;
    }
    
    if (binary % 10 == 0)
        return;
    
    
    vector <long long> divs;
    divs.clear();
    
    for (int i=2; i<=10; i++) {
        long long y = binary;
        
        p = 1;
        long long result = 0;
        while (y > 0) {
            long long r = y % 10;
            result += (r * p);
            y /= 10;
            p *= i;
        }

        long long div = check(result);
        
        if (div == -1) {
            git = false;
            break;
        }
        
        divs.push_back(div);
    }
    
    if (git) {
        printf("%lld ", binary);
        for (int i=0; i<divs.size(); i++)
            printf("%lld ", divs[i]);
        printf("\n");
        ile++;
    }   
}

int main() {
    int t, N, J;
    scanf("%d", &t);
    scanf("%d %d", &N, &J);
    
    int first = 32768;
    int last = 32768 * 2 - 1;
    
    printf("Case #1:\n");
    
    for (int i=first; i<=last; i++) {
        sprawdz(i);
        if (ile == J)
            break;
    }
    
    
    return 0;
}

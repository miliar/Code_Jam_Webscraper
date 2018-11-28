#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <string>
#include <cmath>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);
    
    long long t, k, c, s;
    
    scanf("%lld", &t);
    
    for (int i = 1; i <= t; i++) {
        scanf("%lld%lld%lld", &k, &c, &s);
        
        printf("Case #%d: ", i);
        
        long long min = (k - 1) / c + 1;
        
        if (s < min) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        
        long long currp = 0;
        long long curr = 1;
        long long acc = 0;
        
        
        for (int i = 0; i < k; i++) {
            acc += i * curr;
            
            curr *= k;
            currp++;
            
            if (currp == c || i == k - 1) {
                printf("%lld ", acc + 1);
                acc = 0;
                curr = 1;
                currp = 0;
            }
        }
        
        printf("\n");
    }
    
    return 0;
}
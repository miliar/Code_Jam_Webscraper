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
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    int t;
    
    scanf("%d\n", &t);
    
    for (int i = 1; i <= t; i++) {
        int res = 0;
        char last = getchar();
        
        while (1) {
            char curr = getchar();
            
            if (curr == '\n') {
                res += last == '-';
                break;
            }
            
            res += curr != last;
            last = curr;
        }
        
        printf("Case #%d: %d\n", i, res);
    }
    
    return 0;
}
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

int finded[10];
int counter;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int t = 0;
    
    scanf("%d\n", &t);
    
    for (int i = 1; i <= t; i++) {
        int res = 0;
        
        int x;
        
        scanf("%d", &x);
        
        if (x == 0) {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }
        
        for (int j = 0; j < 10; j++) {
            finded[j] = 0;
        }
        
        counter = 10;
        
        for (int curr = x; ; curr += x) {
            res++;
            int tmp = curr;
            
            while (tmp > 0) {
                int d = tmp % 10;
                
                if (finded[d] == 0) {
                    finded[d] = 1;
                    counter--;
                }
                
                tmp /= 10;
            }
            
            if (counter == 0) {
                printf("Case #%d: %d\n", i, curr);
                break;
            }
        }
    }
    
    return 0;
}
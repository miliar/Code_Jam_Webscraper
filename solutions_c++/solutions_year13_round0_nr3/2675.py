
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>

using namespace std;

typedef unsigned long long ull;

bool is_palindrome (char num[]) {
    int len = strlen(num);
    int m = len/2;
    
    for (int i = 0; i < m; i++) {
        if (num[i] != num[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main (void) {
    int t;
    ull a, b, count, root;
    char num_a[100], num_root[100];
    
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    
    scanf("%d", &t);
    
    for (int z = 1; z <= t; z++) {
        scanf("%llu %llu", &a, &b);
        count = 0;
        
        while (a <= b) {
            root = (ull)sqrt((double)a);
            if (root * root == a) {
                sprintf(num_a, "%llu", a);
                sprintf(num_root, "%llu", root);
            
                if (is_palindrome(num_a) && is_palindrome(num_root)) {
                    count++;
                }
            }
            a++;
        }
        
        printf("Case #%d: %llu\n", z, count);
    }
    
    return 0;
}

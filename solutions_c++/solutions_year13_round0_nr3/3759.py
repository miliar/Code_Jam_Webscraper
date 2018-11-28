#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <cstring>
#define TASK "C"
using namespace std;

int T;
long long A, B;

int digits[100];

bool isPal(long long n) {
    int d;
    for (d = 0; n > 0; n /= 10) {
        digits[d++] = n % 10;
    }
    
    for (int i = 0; i < d / 2; i++) {
        if (digits[i] != digits[d - i - 1]) {
            return false;
        }
    }
    
    return true;
}

int Solve(long long n) {
    int r = 0;
    long long s;
    
    // Oh well...
    
    for (int i = 1; (s = (long long)i * i) <= n; i++) {
        if (isPal(i) && isPal(s)) {
            r++;
        }
    }
    
//    for (int i = 1; i <= 9 && (s = (long long)i * i) <= n; i++) {
//        if (isPal(i) && isPal(s)) {
//            r++;
//            //printf("1 Fair and square: %I64d  ==  %d * %d\n", s, i, i);
//        }
//    }
//    
//    for (int i = 10; i <= 99 && (s = (long long)i * i) <= n; i++) {
//        if (i % 10 < 3) {
//            if (isPal(i) && isPal(s)) {
//                r++;
//                //printf("2 Fair and square: %I64d  ==  %d * %d\n", s, i, i);
//            }
//        }
//    }
//    
//    for (int i = 100; (s = (long long)i * i) <= n; i++) {
//        if ((i % 10 < 3) && (i % 100 <= 11)) {
//            if (isPal(i) && isPal(s)) {
//                r++;
//                //printf("2 Fair and square: %I64d  ==  %d * %d\n", s, i, i);
//            }
//        }
//    }
    
    return r;
}

int main() {
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
    
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        scanf("%I64d %I64d", &A, &B);
        printf("Case #%d: %d\n", test, Solve(B) - Solve(A - 1));
    }
    
    return 0;
}

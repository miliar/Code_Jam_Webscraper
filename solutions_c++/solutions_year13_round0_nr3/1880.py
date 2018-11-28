#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
typedef long long ll;

using namespace std;

bool isPalindrome(ll n) {
    int digits[20], i = 0;
    while(n) {
        digits[i++] = n % 10;
        n /= 10;
    }
    for (int j = i - 1; j >= i / 2; j--) { // i is no. of digits
        if (digits[j] != digits[i - 1 - j]) {
            return false;
        }
    }
    return true;
}

int getFNS(ll start, ll end) { // returns no. of fairAndSquare numbers between start^2 and end^2
    int fns = 0;
    for (ll number = start; number <= end; number++) {
        if (isPalindrome(number)) {
            if (isPalindrome(number*number)) {
                fns++;
            }
        }
    }
    return fns;
}


int main () {
    int t, testcase = 1;
    ll start, end;
    scanf("%d", &t);
    while (testcase <= t) {
        scanf("%lld%lld", &start, &end);
        printf("Case #%d: %d\n", testcase++, getFNS((ll) ceil(sqrt(start)), (ll) sqrt(end)));
    }
    return 0;
}

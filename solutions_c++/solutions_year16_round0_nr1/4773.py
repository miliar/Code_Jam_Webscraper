#include<stdio.h>
#include <set>
#include <cmath>
#define MAXN 1000001
using namespace std;

int N[MAXN];
int ans[MAXN];

int get_kth_digit(int n, int pos) {
    n /= pow(10, pos);
    return n % 10;
}

int get_digit(int n) {
    int retVal = 1;
    while(n /= 10) retVal++;
    return retVal;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t = 1;

    scanf("%d", &t);

    for(int i = 0; i < t; i++) scanf("%d", &N[i]);
    for(int i = 0; i < t; i++) ans[i] = 0;

    for(int i = 0; i < t; i++) {
        set<int> digits;
        set<int>::iterator it;

        if(N[i] == 0) ans[i] = 0;
        else {
            for(int j = 1; digits.size() < 10; j++) {
                int digit = j*N[i];
                int numDigits = get_digit(digit);

                for(int k = 0; k < numDigits; k++) {
                    int nthDigit = get_kth_digit(digit, k);
                    digits.insert(nthDigit);
                }
                ans[i] = digit;
            }
        }
    }

    for(int i = 0; i < t; i++) {
        if(ans[i] == 0)
            printf("Case #%d: INSOMNIA\n", i+1);
        else printf("Case #%d: %d\n", i+1, ans[i]);
    }
}

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define MAX_DIGITS 100

bool isPalindrome(unsigned long long n) {
    if (n == 0) {
        return true;
    }

    int digits[MAX_DIGITS];
    int ndigits = ceil(log10(n));

    // nothing ending in zero can be palindromic
    if (n % 10 == 0) {
        return false;
    }

    for (int j = 0; j < ndigits; j++) {
        digits[j] = n % 10;
        n /= 10;
    }

    // verify palindromic
    for (int j = 0; j < ndigits; j++) {
        if (digits[j] != digits[ndigits-j-1]) {
            return false;
        }
    }

    return true;
}

int main(int argc, char* argv[]) {
    assert(isPalindrome(0));
    assert(isPalindrome(5));
    assert(!isPalindrome(10));
    assert(isPalindrome(11));
    assert(isPalindrome(222));
    assert(isPalindrome(676));
    assert(!isPalindrome(100));
    assert(!isPalindrome(1000));
    assert(isPalindrome(1001));
    assert(isPalindrome(99999999999999));
    assert(isPalindrome(23456789098765432L));
    assert(isPalindrome(87654321012345678L));
    assert(!isPalindrome(012345676543210));

    unsigned long long a, b;

    int ncases;
    scanf("%d", &ncases);

    for (int i = 0; i < ncases; i++) {
        scanf("%llu %llu", &a, &b);

        int count = 0;

        // we need to check squares between a and b
        // i.e. square numbers between sqrt(a) and sqrt(b)
        unsigned long long roota = ceil(sqrt((long double)a));
        unsigned long long rootb = floor(sqrt((long double)b));

        for (unsigned long long n = roota; n <= rootb; n++) {
            // check if n is a palindrome

            if (isPalindrome(n)) {
                unsigned long long nsquared = n*n;
                if (isPalindrome(nsquared)) {
                    //printf("%llu^2 = %llu\n", n, nsquared);
                    count++;
                }
            }
        }

        printf("Case #%d: %d\n", i+1, count);
    }

    return EXIT_SUCCESS;
}
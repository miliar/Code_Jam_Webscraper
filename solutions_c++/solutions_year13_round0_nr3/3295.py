#include <cstdlib>
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string.h>

using namespace std;

class Palindrome {
    
    public:
        Palindrome();
        ~Palindrome();
        
        long scan(register double range_start, register double range_end);
        
    private:
        inline char isFAS(register double x);
        inline char isPAL(register double x);
        
        char digits[15];
};

Palindrome::Palindrome()  {}
Palindrome::~Palindrome() {}

long Palindrome::scan(register double range_start, register double range_end) {

    long count = 0;
    
    double x;
    for (x = range_start; x <= range_end; x++) {
        count += isFAS(x);
    }
    
    return count;
}

char Palindrome::isFAS(register double x) {
    if (isPAL(x)) {
        register long long sq = (long long) sqrt(x);
        if (sq*sq == (long long) x) {
            return isPAL(sq);
        }
    }
    return 0;
}

char Palindrome::isPAL(register double x) {
    sprintf(&digits[0], "%Ld", (long long) x);
    char len = strlen(&digits[0]);
    
    register char l = 0;
    register char r = len-1;
    do {
        if (digits[l] != digits[r]) {
            return 0;
        }
        l++;
        r--;
    } while (l < r);
    
    return 1;
}

int main(int argc, char** argv) {
 
    Palindrome* palindrome = new Palindrome();
    
    int i,T;
    double range_start;
    double range_end;
    
    scanf("%d\n", &T);
    for (i = 0; i < T; i++) {
        scanf("%lf %lf\n", &range_start, &range_end);
        
        printf(
                "Case #%d: %ld\n", 
                i+1, 
                palindrome->scan(range_start, range_end)
        );
    }
    
    delete(palindrome);
    
    return 0;
}


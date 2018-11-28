#include <iostream>
#include <math.h>

bool isPalindrome(int n) {
    int reverse = 0, t = n;
    
    while (t != 0) {
        reverse = reverse * 10;
        reverse = reverse + t % 10;
        t = t / 10;
    }
    
    return (reverse == n);
}

bool isSquareOfPalindrome(int n) {
    double dRoot = sqrt(n);
    int iRoot = dRoot;
    return (dRoot != iRoot) ? 0 : isPalindrome(iRoot);
}

int main(int argc, char **argv) {
    int t = 0;
    std::cin >> t;
    
    for (int i = 0; i < t; i++) {
        int a = 0, b = 0, total = 0;
        std::cin >> a;
        std::cin >> b;
        
        for (int n = a; n <= b; n++) {
            if (isPalindrome(n) && isSquareOfPalindrome(n)) total++;
        }
        
        std::cout << "Case #" << i + 1 << ": " << total << '\n';
    }
    
    return 0;
}
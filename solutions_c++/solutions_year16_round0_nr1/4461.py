#include <string>
#include <iostream>
#include <vector>
#include <set>


inline void 
extractDigits(unsigned long long n, std::set<int>& digits)
{
    while (n > 0) {
        int digit = n % 10;
        n = n / 10;
        digits.insert(digit);
    }
}

unsigned long long
calculate(unsigned long long Ninit)
{
    std::set<int> digits;
    unsigned long long N = Ninit;
    int counter = 0;
    
    while (digits.size() < 10) {
        extractDigits(N, digits);
        N += Ninit;
    }
    
    return N-Ninit;
}


int main(void)
{
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        unsigned long long N;
        std::cin >> N;
        if (N == 0) {
            std::cout << "Case #" << (i+1) << ": " << "INSOMNIA\n";
        } else {
            N = calculate(N);
            std::cout << "Case #" << (i+1) << ": " << N << "\n";
        }
    }

    return 0;
}

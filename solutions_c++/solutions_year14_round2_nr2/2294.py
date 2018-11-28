#include <iostream>
#include <cstdint>
#include <utility>
#include <cmath>

typedef std::uintmax_t int_type;

int_type calc(int_type A, int_type B, int_type K)
{
    int_type accum = 0;
    const int_type min = std::min(A, std::min(B, K));
    accum += min * A + min * B - min * min;
    
    for (int_type k = 0; k < K; k++)
    {
        if (k >= A && k >= B) break;
        for (int_type a = min; a < A; a++)
        {
            for (int_type b = min; b < B; b++)
            {
                if ((a & b) == k) accum++;
            }
        }
    }
    
    return accum;
}

int main()
{

    // Read the number of test cases
    int no_test_cases;
    std::cin >> no_test_cases;
    
    // Debug
    //std::cout << no_test_cases << std::endl;
    
    for (int i = 1; i <= no_test_cases; i++)
    {
    
        int_type A, B, K;
        std::cin >> A;
        std::cin >> B;
        std::cin >> K;
        
        // Debug
        //std::cout << A << " " << B << " " << K << std::endl;
        
        std::cout << "Case #" << i << ": ";
    
        const int_type result = calc(A, B, K);
        std::cout << result << std::endl;
     
    }
    
    return 0;
    
}

#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>


int main()
{
    unsigned n_tests;
    std::cin >> n_tests;
    
    for (unsigned t = 0; t < n_tests; t++)
    {
        typedef std::pair<unsigned, unsigned> two_rows;
        two_rows answer;
        std::vector<two_rows> arrangement(16);

        std::cin >> std::get<0>(answer);
        for (unsigned row = 1; row <= 4; row++)
            for (unsigned col = 1; col <= 4; col++)
            {
                unsigned num;
                std::cin >> num;
                std::get<0>(arrangement[num - 1]) = row;
            }

        std::cin >> std::get<1>(answer);
        for (unsigned row = 1; row <= 4; row++)
            for (unsigned col = 1; col <= 4; col++)
            {
                unsigned num;
                std::cin >> num;
                std::get<1>(arrangement[num - 1]) = row;
            }
        
        unsigned count = 0;
        unsigned number_found = 0;
        for (unsigned i = 0; i < 16; i++)
            if (arrangement[i] == answer)
            {
                count++;
                number_found = i;
            }

        std::cout << "Case #" << t + 1 << ": ";
        if (count == 1)
            std::cout << number_found + 1;
        else if (count > 1)
            std::cout << "Bad magician!";
        else
            std::cout << "Volunteer cheated!";
        std::cout << std::endl;
    }

    return 0;
}

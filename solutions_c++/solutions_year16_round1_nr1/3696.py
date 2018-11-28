#include <iostream>
#include <cstdint>
#include <string>

int main()
{
    int number_of_inputs = 0;

    std::cin >> number_of_inputs;

    std::string S;
    for (int i = 0; i < number_of_inputs; ++i)
    {
        std::cin >> S;
        std::cout << "Case #" << (i + 1) << ": ";
        
        std::string last_word;
        for (const auto& c : S)
        {
            if (last_word.length() == 0)
            {
                last_word += c;
            }
            else if (c < last_word[0])
            {
                last_word += c;
            }
            else
            {
                last_word.insert(0, 1, c);
            }
        }

        std::cout << last_word << std::endl;
    }

    return 0;
}



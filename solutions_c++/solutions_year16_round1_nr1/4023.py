#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    std::string word;
    char last_letter;
    std::string final_word;
    std::cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        std::cin >> word;
        final_word = "";
        for(const auto& s: word)
        {
            if(s<final_word.front())
            {
                final_word += s;
            }
            else if(s>final_word.back())
            {
                final_word = s + final_word;
            }
            else
            {
                final_word += s;
            }
        }
        std::cout << "Case #" << i << ": " << final_word << std::endl;
    }
    return 0;
}

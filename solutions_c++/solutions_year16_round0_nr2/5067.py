#include <iostream>
#include <string>

std::string switchChars(std::string const& original, int position);

int main()
{
    int t;
    std::string input_string;
    std::string::const_iterator ite;
    char last;
    int original_size = 0;
    int size_str;
    int move_nr;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        std::cin >> input_string;
        move_nr = 0;
        while(input_string.find_first_not_of('+') != std::string::npos)
        {
            original_size = input_string.size();
            last = input_string.front();
            size_str = 0;
            for(ite = input_string.begin();ite != input_string.end();++ite)
            {
                if(last != *ite)
                {
                    break;
                }
                last = *ite;
                size_str++;
            }
            input_string = switchChars(input_string,original_size - size_str);
            move_nr++;
        }
        std::cout << "Case #" << i << ": " << move_nr << std::endl;
    }
    return 0;
}

std::string switchChars(std::string const& original, int position)
{
    std::string retval = original;
    int org_size = original.size();
    for(unsigned int i = 0; i < original.size() - position; ++i)
    {
        switch(original[i])
        {
        case '-':
            retval[org_size - i - 1 - position] = '+';
            break;
        case '+':
            retval[org_size - i - 1 - position] = '-';
            break;
        }
    }
    return retval;
}

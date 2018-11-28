#include <iostream>
#include <string>
#include <vector>

bool checkNums(std::vector<bool> digits){

    for (auto v : digits)
    {
        if (v == 0)
        {
            return false;
        }
    }

    return true;
}

int main(int argc, char* argv[])
{
    std::vector<bool> digits (10,0);
    std::string input;
    int j = 1;
    int i = 1;
    int n;
    while (std::cin >> n)
    {
        while (!checkNums(digits))
        {
            if(n == 0)
            {
                std::cout << "Case #" << j << ": " << "INSOMNIA" << std::endl;
                break;
            }
            input = std::to_string(n * i);
            for (long long digit : input)
            {
                if(!digits[digit-48]){
                    digits[digit-48].flip();
                }
            }
            i++;
        }
        if(n != 0)
        {
            std::cout << "Case #" << j << ": " << input << std::endl;
            digits.flip();
        }
        i = 1;
        j++;
    }

    return 0;
}

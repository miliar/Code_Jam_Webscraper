#include <iostream>
#include <string>
#include <sstream>

int main()
{


    std::string _str;
    char buffer[10000], ch;
    int start, end, N;
    std::cin >> N;

    for(int i = 1; i <= N; i++)
    {

        std::cin >> _str;
        // std::stringstream ss(_str);
        std::cout << "Case #" << i << ": ";

        start = 5000; end = 5001;

        buffer[5000] = _str[0];

        // while(ss >> ch)
        for(int j = 1; _str[j] != '\0'; ++j)
        {
            if(_str[j] < buffer[start])
            {
                // buffer[end] = ch;
                buffer[end] = _str[j];
                end++;
            }
            else
            {
                // buffer[start-1] = ch;
                buffer[start-1] = _str[j];
                start--;
            }
        }

        for(int j = start; j < end; j++)
            std::cout << buffer[j];

        std::cout << std::endl;

    }

    return 0;

}

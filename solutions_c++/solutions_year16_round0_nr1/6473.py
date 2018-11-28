#include <iostream>
#include <bitset>
#include <sstream>

std::string to_string(long int N)
{
    std::ostringstream ss;
    ss << N;
    return ss.str();
}

int main()
{
    int T;
    std::cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        int N;
        std::cin >> N;
        std::bitset<10> marker;
        int j;
        bool found = false;
        for (j = 1; j < 1000; ++j)
        {
            std::string numStr = to_string(N*j);
            for (char a : numStr)
            {
                marker[a-48] = 1;
            }
            if (marker.all())
            {
                found = true;
                break;
            }
        }
        std::cout << "Case #" << i << ": ";
        if (found)
        {
            std::cout << N*j << std::endl;
        }
        else
        {
            std::cout << "INSOMNIA" << std::endl;
        }
    }
}

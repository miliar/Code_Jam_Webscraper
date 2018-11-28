#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream in("in");
    std::ofstream o("out");

    int nb(0);
    in >> nb;

    for(int i(0); i < nb; i++)
    {
        std::string test;
        char c('+');
        int out(0);

        in >> test;

        for(int i(1); i <= test.size(); i++)
        {
            if(c != test[test.size()-i])
            {
                out++;
                if(c == '+')
                {
                    c = '-';
                }
                else
                {
                    c = '+';
                }
            }
        }

        o << "Case #" << i+1 << ": " << out << std::endl;
    }

    return 0;
}

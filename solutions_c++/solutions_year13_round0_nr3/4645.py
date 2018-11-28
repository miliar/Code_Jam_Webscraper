#include <iostream>
#include <string>
#include <sstream>
#include <math.h>
#include <fstream>

bool isPal (long n)
{
    std::ostringstream convert;
    convert << n;
    std::string s = convert.str();

    for (int i = 0; i < s.size()/2; i++)
    {
        if (s[i] != s[s.size() - 1 - i])
            return false;
    }

    return true;
}

int main (void)
{
    std::ofstream f("out.txt");
    
    int T;

    std::cin >> T;

    for (int i = 1; i <= T; i++)
    {
        int count = 0;
        int x;
        int y;
    
        std::cin >> x;
        std::cin >> y;

        int start = (int)sqrt(x);

        if ((double)start < sqrt(x))
            start++;

        int end = (int)sqrt(y);

        for (int j = start; j <= end; j++)
        {
            if (isPal(j))
            {
                if (isPal(long(j) * long(j)))
                {
                    count++;
                }
            }
        }

        f << "Case #" << i << ": " << count << std::endl;
    }
    f.close();

    return 0;
}

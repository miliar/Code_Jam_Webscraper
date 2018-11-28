#include <iostream>
#include <string>

int calcul(int max, std::string s)
{
    int c = 0;
    for (int i = 0, f = 0; i < max + 1; ++i)
    {
        int si = s[i] - '0';
        if (si > 0)
        {
            if (f < i)
            {
                c += i - f;
                f = i;
            }
            f += si;
        }
    }
    return c;
}

int main()
{
    int T = 0;
    std::cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int max = 0;
        std::string s = "";
        std::cin >> max >> s;
        std::cout << "Case #" << i + 1 << ": " << calcul(max, s) << std::endl;
    }
    return 0;
}

#include <iostream>
#include <string>

int NextNot(const std::string & s, int curr, char c)
{
    while(curr < s.size() && s[curr] == c) curr++;
    return curr;
}


int main()
{
    int T;
    std::cin >> T;
    for(int t=0; t<T; t++)
    {
        std::string s;
        std::cin >> s;
        int tot = 0;
        int nm = NextNot(s, 0, '-');
        int np;
        while(true)
        {
            if (nm == s.size())
            {
                tot ++;
                break;
            }
            np = NextNot(s, nm, '+');
            if (nm == 0)
            {
                if (np == s.size())
                    break;
                else
                {
                    tot ++;
                    nm = NextNot(s, np, '-');
                }
            }
            else
            {
                if (np == s.size())
                {
                    tot ++;
                    break;
                }
                else
                {
                    tot += 2;
                    nm = NextNot(s, np, '-');
                }
            }
        }
        std::cout << "Case #" << (t+1) << ": " << tot << std::endl;
    }
    return 0;
}

/**
  * URL: https://code.google.com/codejam/
  * Task: Google Code Jam / Problem B. Revenge of the Pancakes
  * Solution:
  **/

#include <iostream>
#include <vector>
#include <string>

void swp(std::string& s, unsigned from, unsigned to);
int solve(std::string& s, unsigned from, unsigned to, char sign);

int main()
{
    int t;
    std::cin >> t;
    for ( int i = 1; i <= t; ++i )
    {
        std::string s;
        std::cin >> s;

        int result = solve(s, 0, s.size() - 1, '+');
        std::cout << "Case #" << i << ": " << result << std::endl;
    }

    return 0;
}

int solve(std::string& s, unsigned from, unsigned to, char sign)
{
    if ( to == 0 )  return (s[0] != sign);

    unsigned i = to + 1;
    for ( ; i > 0 && s[i - 1] == sign; --i );

    if ( i == 0 )   return 0;
    if ( i == 1 )   return (s[0] != sign);

    int result = 0;
    if ( s[i - 1] != sign && s[0] == sign )
    {
        result += solve(s, from, i - 2, sign == '+' ? '-' : '+');
        swp(s, from, i - 1);
        ++result;
    }
    else
    {
        swp(s, from, i - 1);
        ++result;
        result += solve(s, from, i - 2, sign);
    }

    return result;
}

void swp(std::string& s, unsigned from, unsigned to)
{
    for ( unsigned i = from; i <= (from + to) / 2; ++i )
        std::swap(s[i], s[to + from - i]);

    for ( unsigned i = from; i <= to; ++i )
        s[i] = (s[i] == '+' ? '-' : '+');
}

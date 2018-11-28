#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>

bool is_pal(long long x)
{
    std::string s = "";
    while (x != 0)
    {
        s = (char)(x % 10 + (int)'0') + s;
        x /= 10;
    }
    for (int i = 0; i < s.length() / 2; ++i)
    {
        if (s[i] != s[s.length() - 1 - i])
        {
            return false;
        }
    }
    return true;
}

int main()
{
    std::ifstream in("C-large-1.in");
    std::ofstream out("test.out");
    long long max_input_sqrt = 10000000;
    std::vector<long long> a;
    long long tmp;
    for (long long i = 1; i <= max_input_sqrt; ++i)
    {
        tmp = i * i;
        if (is_pal(i) && is_pal(tmp))
        {
            a.push_back(tmp);
        }
    }
    //std::copy(a.begin(), a.end(), std::ostream_iterator<long long>(std::cout, " "));
    int t;
    in >> t;
    for (int q = 1; q <= t; ++q)
    {
        long long x, y;
        in >> x >> y;
        out << "Case #" << q << ": " << upper_bound(a.begin(), a.end(), y) -
               lower_bound(a.begin(), a.end(), x) << std::endl;
    }
    return 0;
}


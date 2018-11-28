#include <iostream>
#include <string>

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        int res = 0;
        int smax;
        std::string s;
        std::cin >> smax >> s;
        int count = 0;
        for (int i = 0 ; i <= smax ; ++i)
        {
            int n = s[i] - '0';
            if (n > 0)
            {
                if (count < i)
                {
                    int d = i - count;
                    count += d;
                    res += d;
                }
                count += n;
            }
        }
        std::cout << "Case #" << t << ": ";
        std::cout << res;
        std::cout << "\n";
    }
	return 0;
}


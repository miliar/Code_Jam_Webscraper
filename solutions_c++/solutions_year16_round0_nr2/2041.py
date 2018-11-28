#include <iostream>
#include <string>

int f(const std::string &s)
{
    int r = 0;
    char last = '0';
    for (size_t i = 0 ; i < s.size() ; ++i)
    {
        if (s[i] == '+' && last == '-')
            ++r;
        else if (s[i] == '-' && last == '+')
            ++r;
        last = s[i];
    }
    if (s.back() == '-')
        ++r;
    return r;
}

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        std::string s;
        std::cin >> s;
        int r = f(s);
        std::reverse(s.begin(), s.end());
        r = std::min(r, f(s) + 1);
		std::cout << "Case #" << t << ": " << r << "\n";
	}
	return 0;
}


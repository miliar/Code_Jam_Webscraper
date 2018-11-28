#include <iostream>
#include <string>
#include <algorithm>

bool check(std::string s)
{
    std::string r;
    if (s.size() == 1)
        return true;
    for (size_t i = 0 ; i < s.size() ; i += 2)
    {
        char c1 = s[i];
        char c2 = s[i + 1];
        if (c1 > c2)
            std::swap(c1, c2);
        if (c1 == 'P')
        {
            if (c2 == 'R')
                r += 'P';
            else if (c2 == 'S')
                r += 'S';
            else
                return false;
        }
        else if (c1 == 'R')
        {
            if (c2 == 'S')
                r += 'R';
            else
                return false;
        }
        else
            return false;
    }
    return check(r);
}

std::string find(int r, int p, int s)
{
    std::string res;
    std::string str = std::string(p, 'P') + std::string(r, 'R') + std::string(s, 'S');
    do
    {
        if (check(str))
        {
            if (res.empty() || str < res)
                res = str;
        }
    }
    while (std::next_permutation(str.begin(), str.end()));
    if (res.empty())
        res = "IMPOSSIBLE";
    return res;
}

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        int n, r, p, s;
        std::cin >> n >> r >> p >> s;
        int c = 1 << n;
        if (r == c || p == c || s == c
            || (n > 1 && (r == 0 || p == 0 || s == 0)))
        {
    		std::cout << "Case #" << t << ": " << "IMPOSSIBLE\n";
        }
        else
        {
            bool ok = true;
            std::string res = find(r, p, s);
            /*
            while (c > 0 && ok)
            {
                if (c == 2)
                {
                    res += "PR";
                    c -= 2;
                    --p;
                    --r;
                }
                else if (c == 4)
                {
                    res += "PRPS";
                    c -= 4;
                    p -= 2;
                    --r;
                    --s;
                }
                else
                {
                    res += "PRPSRS";
                    c -= 6;
                    p -= 2;
                    r -= 2;
                    s -= 2;
                }
                if (p < 0 || r < 0 || s < 0)
                    ok = false;
            }
            // simulate
            if (ok)
            {
            }
            else
            {
                res = "ERROR";
            }
            */
		    std::cout << "Case #" << t << ": " << res << "\n";
        }
	}
	return 0;
}


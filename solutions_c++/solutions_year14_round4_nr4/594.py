#include <iostream>
#include <vector>
#include <string>
#include <set>

std::string s[1000];

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        int n, m;
        std::cin >> m >> n;
        for (int i = 0 ; i < m ; ++i)
            std::cin >> s[i];

        int res = 0;
        int max = 0;
        std::vector<int> v(m);
        while (true)
        {
            // count
            int all = 0;
            for (int i = 0 ; i < m ; ++i)
                all |= 1 << v[i];
            if (all == (1 << n) - 1)
            {
                int count = 0;
                for (int k = 0 ; k < n ; ++k)
                {
                    std::set<std::string> set;
                    for (int i = 0 ; i < m ; ++i)
                        if (v[i] == k)
                        {
                            for (std::string::iterator j = s[i].begin() ; j != s[i].end() ; ++j)
                                set.insert(std::string(s[i].begin(), j + 1));
                        }
                    count += 1 + set.size();
                }
                if (count > max)
                {
                    max = count;
                    res = 1;
                }
                else if (count == max)
                    ++res;
            }
            // increase
            int i = m - 1;
            while (i >= 0 && v[i] == n - 1)
            {
                v[i] = 0;
                --i;
            }
            if (i < 0)
                break;
            ++v[i];
        }

		std::cout << "Case #" << t << ": " << max << " " << res << "\n";
	}
	return 0;
}


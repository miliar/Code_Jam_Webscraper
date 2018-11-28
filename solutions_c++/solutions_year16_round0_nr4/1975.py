#include <iostream>
#include <vector>

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        long long k, c, s;
        std::cin >> k >> c >> s;
        long long last = 1;
        std::vector<long long> r;
        bool end = false;
        while (s && !end)
        {
            long long i = last - 1;
            if (last == k)
                end = true;
            else
                ++last;
            for (int z = 1 ; z < c ; ++z)
            {
                i = i * k + last - 1;
                if (last == k)
                    end = true;
                else
                    ++last;
            }
            --s;
            r.push_back(i + 1);
        }
		std::cout << "Case #" << t << ": ";
        if (s == 0 && last <= k && !end)
        {
            std::cout << "IMPOSSIBLE";
        }
        else
        {
            for (size_t i = 0 ; i < r.size() ; ++i)
                std::cout << r[i] << " ";
        }
        std::cout << "\n";
	}
	return 0;
}


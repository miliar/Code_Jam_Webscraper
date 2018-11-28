#include <iostream>
#include <vector>

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        int n, x;
        std::cin >> n >> x;
        std::vector<int> v(x + 1);
        for (int i = 0 ; i < n ; ++i)
        {
            int a;
            std::cin >> a;
            ++v[a];
        }

        int res = 0;
        for (int i = x ; i >= 0 ; --i)
        {
            while (v[i])
            {
                --v[i];
                for (int j = i ; j >= 0 ; --j)
                    if (v[j] && i + j <= x)
                    {
                        --v[j];
                        break;
                    }
                ++res;
            }
        }

		std::cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}


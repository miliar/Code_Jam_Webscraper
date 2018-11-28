#include <iostream>
#include <vector>

int v[10000];

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        int n;
        std::cin >> n;
        int max = 0;
        for (int i = 0 ; i < n ; ++i)
        {
            std::cin >> v[i];
            if (v[i] > v[max])
                max = i;
        }
        max = v[max];

        int res = 0;
        int a = 0;
        int b = n - 1;
        while (a < b)
        {
            int min = a;
            for (int i = a ; i <= b ; ++i)
                if (v[min] > v[i])
                    min = i;
            if (min - a < b - min)
            {
                for (int i = min ; i > a ; --i)
                {
                    std::swap(v[i], v[i - 1]);
                    ++res;
                }
                ++a;
            }
            else
            {
                for (int i = min ; i < b ; ++i)
                {
                    std::swap(v[i], v[i + 1]);
                    ++res;
                }
                --b;
            }
        }
        /*
        std::vector<int> inv1(n), inv2(n);

        for (int i = 0 ; i < n ; ++i)
        {
            for (int j = 0 ; j < i ; ++j)
                if (v[j] > v[i])
                    ++inv1[i];
            for (int j = i + 1 ; j < n ; ++j)
                if (v[j] > v[i])
                    ++inv2[i];
        }
        */
        /*
		std::cout << ">>> ";
        for (int i = 0 ; i < n ; ++i)
            std::cout << n - (inv1[i] + inv2[i]) << " ";
        std::cout << "\n";
        */
        /*
        for (int i = 1 ; i < n ; ++i)
            inv1[i] += inv1[i - 1];
        for (int i = n - 2 ; i >= 0 ; --i)
            inv2[i] += inv2[i + 1];
        int w = inv2[0];
        for (int i = 0 ; i < n ; ++i)
        {
            int w1 = inv1[i];
            if (i < n - 1)
                w1 += inv2[i + 1];
            if (w1 < w)
                w = w1;
        }
        res = w;
        */
		std::cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}


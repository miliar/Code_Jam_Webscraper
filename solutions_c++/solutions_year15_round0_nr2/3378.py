#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        int res = 1000000;
        int D;
        std::cin >> D;
        std::vector<int> p(D);
        for (int i = 0 ; i < D ; ++i)
            std::cin >> p[i];
        std::sort(p.begin(), p.end());

        for (int eat = 1 ; eat <= p[D - 1] ; ++eat)
        {
            int r = eat;
            for (int i = 0 ; i < D ; ++i)
            {
                r += p[i] / eat - 1;
                if (p[i] % eat)
                    ++r;
            }
            if (r < res)
                res = r;
        }
        /*for (int i = D - 1 ; i >= 0 ; --i)
        {
            int max_time = p[i];
            int div = 0;
            for (int c = iter ; c <= p[i] ; ++c)
            {
                int cut = p[i] / c - 1;
                if (p[i] % c)
                    ++cut;
                if (max_time >= cut + c)
                {
                    max_time = cut + c;
                    div = cut;
                }
            }
            res += div;
            iter = std::max(iter, max_time - div);
        }
        res += iter;
        */
        /*while (!p.empty())
        {
            std::sort(p.begin(), p.end());
            // split max
            int split = -1;
            int d = (int)p.size();
            int bad = 0;
            for (int i = 0 ; i < d ; ++i)
            {
                if (p[i] / 2 > d - i && p[i] > bad)
                {
                    split = i;
                    break;
                }
                else
                {
                    bad = p[i];
                }
            }
            if (split >= 0)
            {
                for ( ; split < d ; ++split)
                {
                    int h = p[split];
                    p[split] = h / 2;
                    p.push_back((h + 1) / 2);
                    ++res;
                }
                continue;
            }
            // eat min
            int eat = *std::min_element(p.begin(), p.end());
            res += eat;
            for (int i = 0 ; i < (int)p.size() ; ++i)
                p[i] -= eat;
            p.erase(std::remove(p.begin(), p.end(), 0), p.end());
        }*/

		std::cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}


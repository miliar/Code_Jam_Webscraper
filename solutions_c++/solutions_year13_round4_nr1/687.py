#include <iostream>
#include <algorithm>
#include <vector>

struct E
{
    E(int a, int b)
        : x(a), p(b) {}
    int x, p;

    bool operator<(const E& s) const
    {
        if (x != s.x)
            return x < s.x;
        return p > s.p;
    }
};

const long long MOD = 1000002013LL;

typedef std::vector<E> VE;

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        long long res = 0;
        long long sum = 0;
        int n, m;
        std::cin >> n >> m;
        VE v;
        for (int i = 0 ; i < m ; ++i)
        {
            long long o, e, p;
            std::cin >> o >> e >> p;
            v.push_back(E(o, p));
            v.push_back(E(e, -p));

            res = (res + p * ((2 * n - (e - o) + 1) * (e - o) / 2 % MOD)) % MOD;
        }
        std::sort(v.begin(), v.end());
        VE s;
        for (int i = 0 ; i < 2 * m ; ++i)
        {
            if (v[i].p > 0)
            {
                s.push_back(v[i]);
            }
            else
            {
                int p = -v[i].p;
                while (p > 0)
                {
                    long long x = s.back().x;
                    long long d = p;
                    if (s.back().p < d)
                    {
                        d = s.back().p;
                        s.pop_back();
                    }
                    else
                    {
                        s.back().p -= d;
                    }
                    p -= d;
                    x = v[i].x - x;
                    sum = (sum + d * ((2 * n - x + 1) * x / 2 % MOD)) % MOD;
                }
            }
        }
        res = (res - sum + MOD) % MOD;
		std::cout << "Case #" << t << ": " << res << "\n";
	}
	return 0;
}


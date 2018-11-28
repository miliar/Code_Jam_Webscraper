#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;

class Solve
{
public:
    void solve()
    {
        size_t m; cin >> m;
        vector<size_t> S(m+1);

        for (auto& s : S)
        {
            char c; cin >> c;
            s = c - '0';
        }

        size_t t = 0, n = 0;

        for (size_t i = 0; i < S.size(); ++i)
        {
            if (S[i] != 0)
            {
                if (t < i)
                {
                    n += i - t;
                    t = i;
                }

                t += S[i];
            }
        }

        cout << n;
    }
};

int main()
{
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
        Solve s;
		s.solve();
		std::cout << std::endl;
	}
}

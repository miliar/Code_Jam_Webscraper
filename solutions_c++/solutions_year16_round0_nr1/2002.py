#include <iostream>

int main()
{
	int T;
	std::cin >> T;
	for (int t = 1 ; t <= T ; ++t)
	{
        int n;
        std::cin >> n;
        if (n == 0)
        {
    		std::cout << "Case #" << t << ": INSOMNIA\n";
        }
        else
        {
            long long m = n;
            int d = 0;
            while (true)
            {
                long long mm = m;
                while (mm)
                {
                    int dig = (int)(mm % 10);
                    mm /= 10;
                    d |= 1 << dig;
                }
                if (d == 0x3ff)
                    break;
                m += n;
            }
		    std::cout << "Case #" << t << ": " << m << "\n";
        }
	}
	return 0;
}


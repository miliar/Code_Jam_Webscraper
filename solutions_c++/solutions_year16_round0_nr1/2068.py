#include <iostream>
#include <set>
int main()
{
    int testNum;
    std::cin >> testNum;
    for(int testId = 1; testId <= testNum; testId++)
    {
	std::cout << "Case #" << testId << ": ";
	long long x;
	std::cin >> x;
        if (x == 0)
	{
		std::cout << "INSOMNIA" << std::endl;
	}
	else
	{
		int cnt = 0;
		std::set<int> st;
		long long y = x;
		while (st.size() != 10)
		{
			long long tmp = y;
			while (tmp != 0)
			{
				st.insert(tmp % 10);
				tmp /= 10;
			}
			y += x;
			cnt ++;
			std::cerr << cnt << std::endl;
		}
		std::cout << y - x << std::endl;
	}

    }
    return 0;
}


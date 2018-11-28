#include <iostream>
#include <set>
using namespace std;

typedef unsigned long long ull;

int main()
{
	ull x;
	cin >> x;
	for (ull i = 0; i < x; i++)
	{
		ull result = 0;
		ull base;
		cin >> base;
		std::set< ull > s;

		if (base == 0)
			std::cout << "Case #" << i + 1 << ": INSOMNIA" << std::endl;
		else
		{

			while (s.size() != 10)
			{
				result += base;
				ull temp = result;
				while (temp != 0)
				{
					s.insert(temp % 10);
					temp /= 10;
				}
			}


			std::cout << "Case #" << i + 1 << ": " << result << std::endl;

		}
	}
}
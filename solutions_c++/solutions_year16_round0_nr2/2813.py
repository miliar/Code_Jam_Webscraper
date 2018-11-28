#include <iostream>
#include <set>
#include <string>
using namespace std;

typedef unsigned long long ull;

int main()
{
	ull x;
	cin >> x;
	for (ull i = 0; i < x; i++)
	{
		ull result = 0;
		std::string s;
		cin >> s;
		int pos = s.find_last_of('-');
		std::string s2 = s;
		while (pos != -1)
		{
			if (s[0] == '+')
				pos = s.find_first_not_of('+') - 1;
			{
				//std::cout << "Pos: " << pos << std::endl;
				for (int i = 0; i <= pos; i++)
				{
					if (s[pos - i] == '-')
						s2[i] = '+';
					else
						s2[i] = '-';
				}
				s = s2;
			}
			
			//std::cout << s << std::endl;
			pos = s.find_last_of('-');
			result++;
		//	std::cin.get();
		}

			std::cout << "Case #" << i + 1 << ": " << result << std::endl;

		
	}
}
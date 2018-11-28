#include <iostream>
#include <string>
#include <deque>

int main()
{
	int T;
	std::cin >> T;
	for (auto i = 1; i <= T; ++i)
	{
		std::string s;
		std::cin >> s;
		std::deque<char> q;
		for (const auto& c : s)
		{
			if (q.empty() || c >= q.front())
				q.push_front(c);
			else
				q.push_back(c);
		}
		std::cout << "Case #" << i << ": ";
		for (const auto &c : q)
			std::cout << c;
		std::cout << "\n";

	}	
	return 0;
}
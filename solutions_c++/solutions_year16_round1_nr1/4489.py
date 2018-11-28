#include <iostream>
#include <set>
using namespace std;

typedef unsigned long long ull;

int main()
{
	ull x;
	cin >> x;
	for (ull j = 0;  j < x; j++)
	{
		std::string s;
		std::cin >> s;
		std::string f = "";
		std::set< std::string > st;
		st.insert(f);
		std::set< std::string > st2;
		for (int i = 0; i < s.size(); i++)
		{
			for (std::set<std::string>::iterator itr = st.begin(); itr != st.end(); itr++)
			{
				st2.insert(s[i] + *itr);
				st2.insert(*itr + s[i]);
				//std::cout << s[i] + *itr << " " << *itr + s[i] << std::endl;
			}
			st = st2;
			st2.clear();
		}
	//	ull result = 0;

			std::cout << "Case #" << j + 1 << ": " << *st.rbegin() << std::endl;

		
	}
}
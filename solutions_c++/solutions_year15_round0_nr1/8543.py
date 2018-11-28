#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>

int main()
{
	int n;
	std::cin >> n;
	for(int i = 1; i <= n; i++)
	{
		int l;
		std::cin >> l;
		l++;

		std::string str;
		std::cin >> str;
		
		std::vector<int> vec(l);
		for (int j = 0; j < l; j++)
		{
			vec[j] = (str[j] - '0');
		}
		
		int res = 0;
		int up = vec[0];
		for (int j = 1; j < vec.size(); j++)
		{
			if (up < j)
			{
				res += (j - up);
				up += (j - up);
			}
			up += vec[j]; 
		}

		std::cout << "Case #" << i << ": " << res << std::endl;  
	}
}
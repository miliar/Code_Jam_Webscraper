#include <bits/stdc++.h>

void test()
{
	size_t maxshyness;
	std::cin >> maxshyness;
	
	std::string shynesses;
	std::cin >> shynesses;
	
	size_t standing = 0;
	size_t friends = 0;
	for (size_t s = 0; s<=maxshyness; ++s)
	{
		int these = shynesses[s]-'0';
		if (these>0)
		{
			if (standing >= s) {}//alright
			else
			{
				friends += s - standing;
				standing = s;
			}
			
			standing += these;
		}
	}
	
	std::cout << friends;
}

int main()
{
	size_t c;
	std::cin >> c;
	for (size_t i = 1; i<=c; ++i)
	{
		std::cout << "Case #" << i << ": ";
		test();
		std::cout << std::endl;
	}
}

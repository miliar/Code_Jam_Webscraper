#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

int main()
{
	std::ifstream file("A-small-attempt0.in");
	std::ofstream out("out.txt");
	// std::string line;
	// file >> line;
	// std::cout << 42 << std::endl;
	// std::cout << "!" << line << "!" << atoi(line.c_str()) << std::endl;
	int tests;					// = atoi(line.c_str());

	file >> tests;
	std::cout << tests << std::endl;
	for (int i = 0; i < tests; ++i)
	{
		int row = 0;
		std::vector < int >first;
		file >> row;

		for (int j = 0; j < 4; ++j)
		{
			int a, z, e, r;
			file >> a >> z >> e >> r;
			if (j+1 == row)
			{
				first.push_back(a);
				first.push_back(z);
				first.push_back(e);
				first.push_back(r);
			}
         //std::cout << a << " " << z << " " << e << " " << r << std::
					//endl;
		}

		std::vector < int >second;
		file >> row;

		for (int j = 0; j < 4; ++j)
		{
			int a, z, e, r;
			file >> a >> z >> e >> r;
			if (j+1 == row)
			{
				second.push_back(a);
				second.push_back(z);
				second.push_back(e);
				second.push_back(r);
			}
		}
		std::vector < int >res(4);
        std::sort(first.begin(),first.end());
        std::sort(second.begin(),second.end());

		auto it =
			std::set_intersection(first.begin(), first.end(), second.begin(),
								  second.end(), res.begin());
		res.resize(it - res.begin());
		out << "Case #" << i+1 << ": ";
		if (res.size() == 0)
			out << "Volunteer cheated!" << std::endl;
		else if (res.size() == 1)
			out << res[0] << std::endl;
		else
			out << "Bad magician!" << std::endl;
	}
}
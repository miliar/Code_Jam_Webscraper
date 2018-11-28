#include <fstream>
#include <string>

std::string solve(const std::string& str)
{
	std::string res;
	for (auto iter = str.cbegin(); iter != str.cend(); ++iter)
	{
		if (res.empty())
		{
			res.push_back(*iter);
		}
		else
		{
			if (res.front() > *iter)
			{
				res.push_back(*iter);
			}
			else
			{
				res.insert(0, 1, *iter);
			}
		}
	}
	return res;
}

void main()
{
	std::ifstream in("D:\\GoogleCodeJam2016\\input.txt");
	std::ofstream out("D:\\GoogleCodeJam2016\\output.txt");

	size_t count = 0;
	in >> count;
	if (0 > count)
	{
		count = 0;
	}

	size_t number;
	for (size_t i = 0; i < count && !in.eof(); ++i)
	{
		std::string str;
		in >> str;

		const std::string res = solve(str);

		out << "Case #" << i + 1 << ": ";
		out << res;
		out << std::endl;
	}

	in.close();
	out.close();
}
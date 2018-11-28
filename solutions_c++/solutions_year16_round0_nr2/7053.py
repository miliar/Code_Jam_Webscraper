#include <string>
#include <fstream>

int main()
{
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		std::string stack;
		in >> stack;

		int result = 0;
		for (int i = 1; i < stack.size(); i++)
		{
			if (stack[i - 1] != stack[i])
				result++;
		}

		if (stack.size() > 0 && *(stack.end() - 1) == '-')
			result++;

		out << "Case #" << t << ": " << result << std::endl;
	}

	return 0;
}
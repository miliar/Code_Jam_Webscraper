#include <string>
#include <fstream>
#include <vector>
#include <algorithm>


int main()
{
	std::ifstream in("input.in");
	std::ofstream out("output.txt");
	if (!in)
		return -1;

	unsigned int numCases = 0;
	in >> numCases;
	for (unsigned int i = 1; i <= numCases; i++)
	{
		out << "Case #" << i << ": ";

		std::string _stack;
		in >> _stack;
		std::string stack;
		//Reverse
		stack.resize(_stack.size());
		for (size_t i = 0; i < _stack.size(); i++)
		{
			stack[stack.size() - 1 - i] = _stack[i];
		}

		unsigned int N = 0; //Output; num flips
		
		if (stack.back() == '-')
		{
			N += 1;
			stack.pop_back();
		}

		bool bEncounteredPlus = false;
		while (stack.size() > 0)
		{
			if (stack.back() == '+')
			{
				bEncounteredPlus = true;
			}
			else if (bEncounteredPlus)
			{
				N += 2;
				bEncounteredPlus = false;
			}
			stack.pop_back();
		}

		out << N << std::endl;
	}

	out.close();

	return 0;
}



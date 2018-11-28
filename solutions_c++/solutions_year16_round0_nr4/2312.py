#include <string>
#include <fstream>
#include <vector>
#include <algorithm>


typedef unsigned __int64 uint;


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
		out << "Case #" << i << ":";

		uint K, C, S;
		in >> K >> C >> S;

		for (uint j = 1; j <= S; j++)
		{
			out << ' ' << j;
		}

		out << std::endl;
	}

	out.close();

	return 0;
}



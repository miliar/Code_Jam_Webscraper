#include <fstream>
#include <string>

using namespace std;

int main()
{
	int numberOfCases;
	ifstream in("D-small-attempt0.in");
	ofstream out("output.txt");
	in >> numberOfCases;
	for (int i = 0; i < numberOfCases; i++)
	{
		int original, complexity, students;
		in >> original >> complexity >> students;
		if (original == 1)
		{
			out << "Case #" << i + 1 << ": 1" << endl;
			continue;
		}
		if (complexity == 1)
		{
			if (original > students)
			{
				out << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}
			out << "Case #" << i + 1 << ":";
			for (int tile = 1; tile <= original; tile++)
			{
				out << " " << tile;
			}
			out << endl;
		}
		else
		{
			if ((original + 1) / 2 > students)
			{
				out << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}
			int tile = 2;
			out << "Case #" << i + 1 << ":";
			for (int j = 2; j <= original + 1; j += 2)
			{
				out << " " << tile;
				if (j == original - 1)
				{
					tile += original + 1;
					continue;
				}
				tile += 2 * (original + 1);
			}
			out << endl;
		}
	}
	return 0;
}
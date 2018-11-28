#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned int u32;

int main(int argc, char** argv)
{
	ifstream in;
	ofstream out;

	in.open("input.in");
	out.open("output.out");

	u32 T;
	in >> T;
	++T;

	for (u32 i = 1; i < T; ++i)
	{
		u32 N;
		u32 row[4];

		in >> N;
		for (u32 j = 0; j < 4; ++j)
		{
			for (u32 l, k = 0; k < 4; ++k)
			{
				in >> (N - 1 == j ? row[k] : l);
			}
		}

		in >> N;
		u32 matchcount = 0;
		int result;
		for (u32 j = 0; j < 4; ++j)
		{
			for (u32 l, k = 0; k < 4; ++k)
			{
				in >> l;
				if (N - 1 == j)
				{
					for (u32 m = 0; m < 4; ++m)
					{
						if (row[m] == l) { ++matchcount; result = l; }
					}
				}
			}
		}

		cout << "Case #" << i << ": ";
		out << "Case #" << i << ": ";
		if (0 == matchcount)
		{
			cout << "Volunteer cheated!" << endl;
			out << "Volunteer cheated!" << endl;
		}
		else if (1 == matchcount)
		{
			cout << result << endl;
			out << result << endl;
		}
		else
		{
			cout << "Bad magician!" << endl;
			out << "Bad magician!" << endl;
		}
	}

	out.close();
	in.close();

	getchar();

	return 0;
}


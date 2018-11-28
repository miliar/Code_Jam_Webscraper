#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <fstream>

typedef std::vector<int> tRow;
typedef std::vector<tRow> tMatrix;

std::ifstream in("input.in");
std::ofstream out("output.txt");

void getMatrix(tMatrix& m)
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			in >> m[i][j];
		}
	}
}

void printMatrix(const tMatrix& m)
{
	for (int i = 0; i < 4; ++i)
	{
		for (int j = 0; j < 4; ++j)
		{
			out << m[i][j] << " ";
		}
		out << std::endl;
	}
}

struct take
{
	int row1;
	tMatrix m1;
	int row2;
	tMatrix m2;
	take()
		:row1(0)
		 , m1(4, tRow(4, 0))
		 , row2(0)
		 , m2(4, tRow(4, 0))
	{}
};

int main()
{
	int numOfTC;
	in >> numOfTC;
	std::vector<take> takes(numOfTC);
	int c = 0;
	while (c < numOfTC)
	{
		in >> takes[c].row1;
		getMatrix(takes[c].m1);
		in >> takes[c].row2;
		getMatrix(takes[c].m2);
		++c;
	}
	for (int i = 1; i <= numOfTC; ++i)
	{
		take* t = &(takes[i-1]);
		std::vector<int> result;
		std::sort(t->m1[t->row1-1].begin(), t->m1[t->row1-1].end());
		std::sort(t->m2[t->row2-1].begin(), t->m2[t->row2-1].end());
		std::set_intersection(t->m1[t->row1-1].begin(), t->m1[t->row1-1].end(),
				t->m2[t->row2-1].begin(), t->m2[t->row2-1].end(),
				std::back_inserter(result));
		out << "Case #" << i << ": ";
		if (result.size() < 1)
		{
			out << "Volunteer cheated!\n";
		}
		else if (result.size() > 1)
		{
			out << "Bad magician!\n";
		}
		else
		{
			out << result[0] << "\n";
		}
	}
	return 0;
}

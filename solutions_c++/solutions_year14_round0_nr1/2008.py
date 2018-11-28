#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <iterator>
#include <fstream>

void solveonecase(std::ifstream& in, std::ofstream& out, int casenumber)
{

	std::set<int> fs;
	std::set<int> ss;

	int k;
	in >> k;
	--k;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
		{
			int temp;
			in >> temp;
			if (i == k)
				fs.insert(temp);
		}

	in >> k;
	--k;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
		{
			int temp;
			in >> temp;
			if (i == k)
				ss.insert(temp);
		}


	std::vector<int> intersection;
	std::set_intersection(fs.begin(), fs.end(),
                          ss.begin(), ss.end(),
                          std::back_inserter(intersection));

	out << "Case #" << casenumber <<": ";
	if (intersection.size() == 1)
		out << intersection[0];
	else
		if (intersection.size() > 1)
			out << "Bad magician!";
		else
			out << "Volunteer cheated!";
	out << "\n";


}


void main(void)
{
	std::ifstream in("A-small-attempt0.in");
	std::ofstream out("A-small-attempt0.out");

	int n;
	in >> n;

	for (int i = 0; i < n; ++i)
	{
		solveonecase(in, out, i + 1);
	}
//	std::cout << "ggg";
	
//	std::system("pause");
}
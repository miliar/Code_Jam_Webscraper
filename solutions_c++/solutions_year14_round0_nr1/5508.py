#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define COLS 4
#define ROWS 4
#define MAP_SIZE (COLS*ROWS)

void main()
{
	int T = 0;

	ifstream in("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	in >> T;

	for(int i=0; i<T; ++i)
	{
		vector<int> solve1, solve2;
		int row;
		int el;

		in >> row;

		for(int j=0; j<MAP_SIZE; j++)
		{
			in >> el;

			if(j/4 == row - 1)
				solve1.push_back(el);
		}

		in >> row;

		for(int j=0; j<MAP_SIZE; j++)
		{
			in >> el;

			if(j/4 == row - 1)
			{
				if(find(solve1.begin(), solve1.end(), el)!=solve1.end())
					solve2.push_back(el);
			}
		}

		out << "Case #" << i+1 << ": ";

		if(solve2.size() == 0)
			out << "Volunteer cheated!"<<endl;

		if(solve2.size() == 1)
			out << solve2[0] <<endl;

		if(solve2.size() > 1)
			out << "Bad magician!"<<endl;
	}
}
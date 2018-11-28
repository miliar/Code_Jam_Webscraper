#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool isValid(const std::vector<std::vector<int> >& field)
{
	for(size_t i = 0; i < field.size(); i++)
	{
		for(size_t j = 0; j < field[i].size(); j++)
		{
			int val = field[i][j];

			int mv = 0;
			for(size_t k = 0; k < field.size(); k++)
				if(field[k][j] > mv)
					mv = field[k][j];

			int mh = 0;
			for(size_t k = 0; k < field[i].size(); k++)
				if(field[i][k] > mh)
					mh = field[i][k];

			if(mh > val && mv > val)
				return false;
		}
	}

	return true;
}

int main()
{
	std::ifstream in("B-large.in");
	std::ofstream out("out.txt");
	int n = 0;
	in >> n;

	for(int i = 0; i < n; i++)
	{
		int h = 0, w = 0;
		in >> h;
		in >> w;

		std::vector<std::vector<int> > field;

		for(int j = 0; j < h; j++)
		{
			field.push_back(std::vector<int>());
			for(int k = 0; k < w; k++)
			{
				int g = 0;
				in >> g;
				field[j].push_back(g);
			}
		}

		out << "Case #" << i + 1 << ": ";
		out << (isValid(field) ? "YES" : "NO") << std::endl;
	}	

	in.close();
	out.close();
	return 0;
}
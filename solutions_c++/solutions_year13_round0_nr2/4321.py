#include <fstream>
#include <iostream>
#include <vector>

class Lawn
{
	std::vector<int> map;
	int w;
	int h;

public:
	Lawn(std::ifstream & ifs)
	{
		ifs >> h >> w;
		

		for(int x = 0; x < w; x++)
		{
			for(int y = 0; y < h; y++)
			{
				int in;
				ifs >> in;
				map.push_back(in);
			}
		}
	}

	bool minRow(int x, int y)
	{
		int pos = map[x+w*y];
		bool result = true;
		for(int x = 0; x < w; x++)
		{
			if(map[x+w*y] > pos)
			{
				//std::cout << x << "," << y << " " << map[x+w*y] << " > " << pos << std::endl;
				return false;
			}
		}
		return true;
	}

	bool minCol(int x, int y)
	{
		int pos = map[x+w*y];
		bool result = true;
		for(int y = 0; y < h; y++)
		{
			if(map[x+w*y] > pos)
			{
				//std::cout << x << "," << y << " " <<map[x+w*y] << " > " << pos << std::endl;
				return false;
			}
		}
		return true;
	}

	bool doable()
	{
		for(int x = 0; x < w; x++)
		{
			for(int y = 0; y < h; y++)
			{

				if(!minCol(x,y) && !minRow(x,y))
				{
					//std::cout << x << "," << y << " " <<std::endl;//<< minCol(x,y) << " ||" << minRow(x,y) << std::endl;
					return false;
				}
			}
		}
		return true;
	}

};

int main()
{
	std::ifstream ifs ("B-large.in");
	std::ofstream ofs("a.out");

	int number;

	ifs >> number;

	for(int i = 0; i < number ;i++)
	{
		Lawn l(ifs);

		ofs << "Case #" << (i+1) <<": ";

		ofs << (l.doable()?"YES":"NO");

		ofs << std::endl;

	}
	return 0;
}
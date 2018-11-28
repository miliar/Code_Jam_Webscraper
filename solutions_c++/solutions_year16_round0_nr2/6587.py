#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	int T;
	ifstream ifs;
	ifs.open("B-large.in",ios::in);
	ofstream os("haha.txt");
	ifs >> T;
	int index = 0;
	string line;
	int size;
	int count;
	bool positive;
	while (index < T)
	{
		index++;
		ifs >> line;
		size = line.size();
		count = 0;
		positive = (line[0] == '+');
		count++;
		for (int i = 1; i < size; i++)
		{
			if (positive)
			{
				if (line[i] == '-')
				{
					positive = false;
					count++;
				}
			}
			else
			{
				if (line[i] == '+')
				{
					positive = true;
					count++;
				}
			}

		}
		if (line[size - 1] == '+')
		{
			count--;
		}
		os << "Case #" << index << ": " << count << endl;
		
	}
	ifs.close();
	os.close();
}

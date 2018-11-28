#include <iostream>
#include <vector>
#include <limits>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iomanip> 
#include <fstream>

using namespace std;

int main()
{
	ifstream ins("C:\\Users\\Mike\\Downloads\\A-small-attempt1 (1).in");
	int t;
	ins >> t;

	for(int g = 0; g < t; g++)
	{
		int poss[4];
		int poss2[4];
		int f, j;
		ins >> f;
		for(int i = 0; i < (f - 1) * 4; i++)
			ins >> j;
		for(int i = 0; i < 4; i++)
			ins >> poss[i];
		for(int i = f * 4; i < 16; i++)
			ins >> j;
		ins >> f;
		for(int i = 0; i < (f - 1) * 4; i++)
			ins >> j;
		for(int i = 0; i < 4; i++)
			ins >> poss2[i];
		for(int i = f * 4; i < 16; i++)
			ins >> j;
		int count = 0;
		int c = -1;
		for(int i = 0; i < 4; i++)
		{
			for(int k = 0; k < 4; k++)
			{
				if(poss[i] == poss2[k])
				{
					count++;
					c = poss[i];
				}
			}
		}
		if(count == 0)
			cout << "Case #" << (g + 1) << ": Volunteer cheated!" << endl;
		else if(count == 1)
			cout << "Case #" << (g + 1) << ": " << c << endl;
		else
			cout << "Case #" << (g + 1) << ": Bad magician!" << endl;
	}
	cin.get();cin.get();
	return 0;
}
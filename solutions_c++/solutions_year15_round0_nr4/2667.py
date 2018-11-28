#include <fstream>
#include <vector>
#include <algorithm>
#include <map>


using namespace std;


typedef unsigned int UINT;


int main()
{
	ifstream input("input.in");
	ofstream output("output.txt");
	UINT nCases = 0;
	input >> nCases;
	for (UINT _case = 0; _case < nCases; _case++)
	{
		output << "Case #" << _case + 1 << ": ";

		UINT Omino, Width, Height;
		input >> Omino;
		input >> Width;
		input >> Height;

		if (Omino > Width * Height)
			goto R;
		if (Omino == 1)
			goto G;
		if (Omino % 2 == 0)
		{
			if ((Width * Height) % 2 != 0)
				goto R;
			if (Omino == 2)
				goto G;
		}
		if (Omino > 2 && (Width == 1 || Height == 1))
			goto R;
		if (Omino == 3)
		{
			if (Width * Height == 16)
				goto R;
			if (Width + Height == 7) //3 by 4
				goto G;
			if (Width == 3 && Height == 3)
				goto G;
			if (Width * Height == 6)
				goto G;
			if (Width == 2 && Height == 2)
				goto R;
			if (Width * Height == 8)
				goto R;
		}
		if (Omino == 4)
		{
			if (Width * Height == 16 || Width * Height == 12)
				goto G;
			else goto R;
		}

		if ((float)(Height * Width) / (float)Omino != 0.0f)
			goto R;


	R:
		output << "RICHARD" << endl;
		continue;
	G:
		output << "GABRIEL" << endl;
		continue;
	}
	input.close();
	output.close();
	return 0;
}



#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <stdlib.h> 

using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	output.open("codejam3s.out");
	input.open("input.in");
	int M[4][4] = {{1,2,3,4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};

	int T;
	input >> T;
	for (int l = 0; l < T; ++l)
	{
		int L, X;
		input >> L >> X;

		string str, tstr;
		input >> str;
		tstr = str;

		for (int i = 1; i < X; ++i)
		{
			str += tstr;
		}
		int size = str.size();
		int** D;
		D = (int **)malloc(sizeof(char*)*size);
		for (int i = 0; i < size; ++i)
		{
			D[i] = (int*) malloc(sizeof(char*)*size);
		}

		for (int i = 0; i < str.size(); ++i)
		{
			for (int j = i; j < str.size(); ++j)
			{
				if(i==j)
				{
					D[i][j] = str[i]-'g';
				}
				else
				{
					if(D[i][j-1] > 0)
					{
						D[i][j] = M[D[i][j-1]-1][str[j]-'g'-1];
					}
					else
					{
						D[i][j] = M[(int)abs(D[i][j-1])-1][str[j]-'g'-1]*(-1);
					}
				}
			}
		}

		bool done = false;
		for (int i = 0; i < str.size()-2; ++i)
		{
			if(D[0][i] == 2)
			{
				for (int j = i+1; j < str.size()-1; ++j)
				{
					if(D[i+1][j] == 3)
					{
						if(D[j+1][str.size()-1] == 4)
						{
							output << "Case #" << l+1 << ": YES" << endl;
							done = true;
							break;
						}
					}
				}
				if(done)
					break;
			}
		}
		if(!done)
		output << "Case #" << l+1 << ": NO"<< endl;

		for (int i = 0; i < size; ++i)
		{
			delete [] D[i];
		}
		delete [] D;
	}

	return 0;

}
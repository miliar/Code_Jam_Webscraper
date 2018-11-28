#include <fstream>
#include <string>
using namespace std;

int main()
{
	unsigned int		T, iIndex = 0, N;

	ifstream	InFile("A-large.in");
	ofstream	OutFile("A-large.out", ios_base::ate || ios_base::out);

	if (OutFile.is_open() && InFile.is_open())
	{
		InFile >> T;

		while (T--)
		{
			int			arrFoundChars['Z' - 'A' + 1] = {0}; 
			int			countNumsFound['9' - '0' + 1] = {0};
			string		strNum;
			char		Distinguishing['9' - '0'] = {'Z', 'O', 'W', 'T', 'U', 'F', 'X', 'S', 'G'};
			string		Nums['9' - '0'] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT"};
			
			InFile >> strNum;

			for (int i = 0; i < strNum.length(); ++i)
				++arrFoundChars[strNum[i] - 'A'];


			for (int i = 0; i < 2; ++i)
			{
				for (int ii = i; ii < 9; ii+= 2)
				{
					countNumsFound[ii] = arrFoundChars[Distinguishing[ii] - 'A'];

					for (int iii = 0; iii < countNumsFound[ii]; ++iii)
					{
						for (int iiii = 0; iiii < Nums[ii].length(); ++iiii)
							--arrFoundChars[Nums[ii][iiii] - 'A'];
					}
				}
			}


			for (int i = 0; i < ('Z' - 'A' + 1); ++i)
			{
				if (arrFoundChars[i] != 0)
				{
					countNumsFound[9] += arrFoundChars[i];
					break;
				}
			}

			OutFile << "Case #" << ++iIndex << ": ";

			for (int i = 0; i < 10; ++i)
			{
				for (int ii = 0; ii < countNumsFound[i]; ++ii)
					OutFile << i;
			}

			OutFile << endl;
		}
	}

	return 0;
}
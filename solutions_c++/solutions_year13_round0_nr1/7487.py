#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

#define fileInput
//#define cInput

int main()
{
	int cases;
	string line;
	unsigned __int32 xboard = 0;
	unsigned __int32 oboard = 0;
	int pieceCount = 0;
	bool winflag = false;
	const unsigned __int32 wins[10] = {15, 240, 3840, 61440, 34952, 17476, 8738, 4369, 33825, 4680};

	fstream fout;
	fout.open("output.txt", fstream::out);

#ifdef fileInput
	fstream finput;
	finput.open("A-large.in", fstream::in);
	finput >> cases;
#endif

#ifdef cInput
	cin >> cases;
#endif

	int totalCases = cases;

	while(cases)
	{
		for(int i = 0; i < 4; i++)
		{
#ifdef cInput
			cin >> line;
#endif

#ifdef fileInput
			finput >> line;
#endif

			for(int j = 0; j < 4; j++)
			{	
				xboard <<= 1;
				oboard <<= 1;

				if(line[j] == 'X')
				{
					xboard++;
					pieceCount++;
				}
				else if(line[j] == 'O')
				{
					oboard++;
					pieceCount++;
				}
				else if(line[j] == 'T')
				{
					xboard++;
					oboard++;
					pieceCount++;
				}
			}
		}

		for(int j = 0; j < 10; j++)
		{
			unsigned __int32 test1 = xboard & wins[j];
			unsigned __int32 test2 = oboard & wins[j];

			if((xboard & wins[j]) == wins[j])
			{
				cout << "Case #" << totalCases - cases + 1 << ": X won\n";
				fout << "Case #" << totalCases - cases + 1 << ": X won\n";
				winflag = true;
				break;
			}
			else if((oboard & wins[j]) == wins[j])
			{
				cout << "Case #" << totalCases - cases + 1 << ": O won\n";
				fout << "Case #" << totalCases - cases + 1 << ": O won\n";
				winflag = true;
				break;
			}
		}
		if(pieceCount == 16 && winflag == false)
		{
			cout << "Case #" << totalCases - cases + 1 << ": Draw\n";
			fout << "Case #" << totalCases - cases + 1 << ": Draw\n";
		}
		else if(pieceCount < 16 && winflag == false)
		{
			cout << "Case #" << totalCases - cases + 1 << ": Game has not completed\n";
			fout << "Case #" << totalCases - cases + 1 << ": Game has not completed\n";
		}

		pieceCount = 0;
		winflag = false;
		cases--;
	}

#ifdef fileInput
		finput.close();
#endif

	fout.close();

	return 0;
}


#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void main()
{
	ifstream Input;
	ofstream Output;
	Input.open("D-small-attempt2.in");
	Output.open("D-small-attempt2.out");

	int Count;

	int i;
	Input >> Count;
	Count += 1;

	for (i = 1; i < Count; i++)
	{
		bool bRichardWin = true;
		int Omino ,R ,C;
		Input >> Omino >> R >> C;

		switch(Omino)
		{
		case 1:
			bRichardWin = false;
			break;
		case 2:
			if((R * C) % 2 == 0)
			{
				bRichardWin = false;
			}
			break;
		case 3:
			if(R > 1 && C > 1)
			{
				if(R == 3 || C == 3)
				{
					bRichardWin = false;
				}
			}
			break;
		case 4:
			if(R * C >= 12)
			{
				bRichardWin = false;
			}
			break;
		default:
			break;
		}

		if(bRichardWin)
		{
			Output << "Case #" << i <<": RICHARD"<< endl;
		}
		else
		{
			Output << "Case #" << i <<": GABRIEL"<< endl;
		}
	}

	return;
}

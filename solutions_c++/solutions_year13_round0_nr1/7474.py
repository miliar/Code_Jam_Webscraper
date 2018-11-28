#include <iostream>
#include <vector>
#include <cstdio>
#include <string>

using namespace std;

bool CheckForX(char ch)
{
	if (ch == 'X' || ch == 'T')
		return true;
	else return false;
}

bool CheckForO(char ch)
{
	if (ch == 'O' || ch == 'T')
		return true;
	else return false;
}

int main()
{
	freopen("A-small.in", "r", stdin);
	int T;
	cin >> T;
	string s1, s2, s3, s4;
	for(int i=1; i<=T; i++)
	{
		cin >> s1 >> s2 >> s3 >> s4;
		bool XWin = false, OWin = false;

		XWin = XWin || (CheckForX(s1[0]) && CheckForX(s1[1]) && CheckForX(s1[2]) && CheckForX(s1[3]));
		XWin = XWin || (CheckForX(s2[0]) && CheckForX(s2[1]) && CheckForX(s2[2]) && CheckForX(s2[3]));
		XWin = XWin || (CheckForX(s3[0]) && CheckForX(s3[1]) && CheckForX(s3[2]) && CheckForX(s3[3]));
		XWin = XWin || (CheckForX(s4[0]) && CheckForX(s4[1]) && CheckForX(s4[2]) && CheckForX(s4[3]));
		XWin = XWin || (CheckForX(s1[0]) && CheckForX(s2[1]) && CheckForX(s3[2]) && CheckForX(s4[3]));
		XWin = XWin || (CheckForX(s4[0]) && CheckForX(s3[1]) && CheckForX(s2[2]) && CheckForX(s1[3]));

		OWin = OWin || (CheckForO(s1[0]) && CheckForO(s1[1]) && CheckForO(s1[2]) && CheckForO(s1[3]));
		OWin = OWin || (CheckForO(s2[0]) && CheckForO(s2[1]) && CheckForO(s2[2]) && CheckForO(s2[3]));
		OWin = OWin || (CheckForO(s3[0]) && CheckForO(s3[1]) && CheckForO(s3[2]) && CheckForO(s3[3]));
		OWin = OWin || (CheckForO(s4[0]) && CheckForO(s4[1]) && CheckForO(s4[2]) && CheckForO(s4[3]));
		OWin = OWin || (CheckForO(s1[0]) && CheckForO(s2[1]) && CheckForO(s3[2]) && CheckForO(s4[3]));
		OWin = OWin || (CheckForO(s4[0]) && CheckForO(s3[1]) && CheckForO(s2[2]) && CheckForO(s1[3]));

		for (int j=0; j<4; j++)
		{
			XWin = XWin || (CheckForX(s1[j]) && CheckForX(s2[j]) && CheckForX(s3[j]) && CheckForX(s4[j]));
			OWin = OWin || (CheckForO(s1[j]) && CheckForO(s2[j]) && CheckForO(s3[j]) && CheckForO(s4[j]));
		}

		if(XWin == true)
		{
			cout << "Case #" << i << ": X won" << endl;
		}
		else if(OWin == true)
		{
			cout << "Case #" << i << ": O won" << endl;
		}
		else
		{
			bool dotPresent = false;
			for(int j=0; j<4; j++)
			{
				if(s1[j] == '.' || s2[j] == '.' || s3[j] == '.' || s4[j] == '.')
				{
					dotPresent = true;
					break;
				}
			}
			if(dotPresent == true)
			{
				cout << "Case #" << i << ": Game has not completed" << endl;
			}
			else
				cout << "Case #" << i << ": Draw" << endl;
		}
	}

















}

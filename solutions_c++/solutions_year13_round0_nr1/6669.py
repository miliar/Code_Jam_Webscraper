#include <iostream>

using namespace std;
char tab[4][4];

bool isIncomplete = false;
bool OWin = false;
bool XWin = false;

int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;
	cin.get();
	for(int z = 1; z <= n; z++)
	{

		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
				cin.get(tab[i][j]);
			cin.get();
		}

		bool XSkos = true, OSkos = true;
		bool XSkosDrugi = true, OSkosDrugi = true;
		for(int i = 0; i < 4; i++)
		{
			bool XWinPoziomo = true, OWinPoziomo = true, XWinPionowo = true, OWinPionowo = true;


			for(int j = 0; j < 4; j++)
			{
				if(!isIncomplete && tab[i][j] == '.') //mamy kropke wiec nie moze gra byæ skoñczona
					isIncomplete = true;
			
				//sprawdzamy poziomo
				if(tab[i][j] == '.')
					XWinPoziomo = OWinPoziomo = false;
				else if(tab[i][j] != 'X' && tab[i][j] != 'T') //mamy X lub T
					XWinPoziomo = false;
				else if(tab[i][j] != 'O' && tab[i][j] != 'T')
					OWinPoziomo = false;

				//sprawdzamy pionowo
				if(tab[j][i] == '.')
					XWinPionowo = OWinPionowo = false;
				else if(tab[j][i] != 'X' && tab[j][i] != 'T') //mamy X lub T
					XWinPionowo = false;
				else if(tab[j][i] != 'O' && tab[j][i] != 'T')
					OWinPionowo = false;

				if(j == i) //mamy skos prawo
				{
					if(tab[i][j] == '.')
						XSkos = OSkos = false;
					else if(tab[j][i] != 'X' && tab[j][i] != 'T') //mamy X lub T
						XSkos = false;
					else if(tab[j][i] != 'O' && tab[j][i] != 'T')
						OSkos = false;
				}
				else if(i + j == 3)
				{
					if(tab[i][j] == '.')
						XSkosDrugi = OSkosDrugi = false;
					else if(tab[i][j] != 'X' && tab[i][j] != 'T') //mamy X lub T
						XSkosDrugi = false;
					else if(tab[i][j] != 'O' && tab[i][j] != 'T')
						OSkosDrugi = false;
				}
			}

			if(XWinPoziomo || XWinPionowo)
			{
				XWin = true;
				OWin = OSkos = OSkosDrugi = false;
				break;
			}
			else if(OWinPionowo || OWinPoziomo)
			{
				OWin = true;
				XWin = XSkos = XSkosDrugi = false;
				break;
			}
		}

		if(XWin || XSkos || XSkosDrugi)
			cout << "Case #" << z << ": X won\n";
		else if(OWin || OSkos || OSkosDrugi)
			cout << "Case #" << z << ": O won\n";
		else if(!isIncomplete)
			cout << "Case #" << z << ": Draw\n";
		else if(isIncomplete)
			cout << "Case #" << z << ": Game has not completed\n";

		XSkos = true, OSkos = true;
		XSkosDrugi = true, OSkosDrugi = true;
		isIncomplete = false;
		OWin = false;
		XWin = false;

		cin.get();

	}
	return 0;
}
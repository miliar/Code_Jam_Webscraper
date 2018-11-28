#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int matrice1[5][5], matrice2[5][5], linie;
	int prima_linie[5];
	int a_doua_linie[5];
	int linie_comuna[5];
	int nr_teste;
	int nr_elemente_comune;
	int element_comun;
	int counter = 1;

	freopen("magictrick.in", "r", stdin);
	freopen("magictrick.out", "w", stdout);

	cin >> nr_teste;
	while(nr_teste--)
	{
		nr_elemente_comune = 0;

		cin >> linie;
		linie--;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				cin >> matrice1[i][j];
			}

		for(int i = 0; i < 4; ++i)
			prima_linie[i] = matrice1[linie][i];

		cin >> linie;
		linie--;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				cin >> matrice2[i][j];
			}
		for(int i = 0; i < 4; ++i)
			a_doua_linie[i] = matrice2[linie][i];

		cout << "Case #" << counter << ": ";
		counter++;

		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
			{
				if(prima_linie[i] == a_doua_linie[j])
				{
					element_comun = prima_linie[i];
					nr_elemente_comune++;				// e dublu nr asta
				}
			}
			if(nr_elemente_comune > 1)
				cout << "Bad magician!" << endl;
			else if(nr_elemente_comune == 1)
				cout << element_comun << endl;
			else 
				cout << "Volunteer cheated!" << endl; 
				
	}

	return 0;
}
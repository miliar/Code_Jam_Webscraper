#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	fstream plik;
	fstream out;
	out.open("out.txt");
	plik.open("plik.txt");
	int n;
	int tab[4][4];
	vector<int> tab_first(4);
	vector<int> tab_second(4);
	plik >> n;
	for (int i = 0; i<n; i++)
	{
		int first;
		plik >> first;
		for (int j = 0; j<4; j++)
		{
			for (int k = 0; k<4; k++)
			{
				plik >> tab[j][k];
			}
			if (j + 1 == first)
			{
				tab_first[0] = tab[j][0];
				tab_first[1] = tab[j][1];
				tab_first[2] = tab[j][2];
				tab_first[3] = tab[j][3];
			}
		}
		sort(tab_first.begin(), tab_first.begin() + 4);
		int second;
		plik >> second;
		for (int j = 0; j<4; j++)
		{
			for (int k = 0; k<4; k++)
			{
				plik >> tab[j][k];
			}
			if (j + 1 == second)
			{
				tab_second[0] = tab[j][0];
				tab_second[1] = tab[j][1];
				tab_second[2] = tab[j][2];
				tab_second[3] = tab[j][3];
			}
		}
		sort(tab_second.begin(), tab_second.begin() + 4);
		int c = 0;
		int w;
		for (int j = 0; j<4; j++)
		{
			for (int k = 0; k<4; k++)
			{
				if (tab_first[j] == tab_second[k])
				{
					c++;
					w = tab_first[j];
				}
			}
		}

		if (c>1)
		{
			out << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
		else
		{
			if (c == 1)
			{
				out << "Case #" << i + 1 << ": " << w << endl;
			}
			else
				out << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
	}
}

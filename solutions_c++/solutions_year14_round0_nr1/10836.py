#include <fstream>
#include <iostream>

using namespace std;

ifstream f ("date.in");
ofstream g ("date.out");

int v[20], a[10][10];
int k = 0, t, x;

int main ()
{
	f >> t;
	for (int l = 1; l <= t; l++)
	{
		f >> x;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				f >> a[i][j];
			
		for (int i = 1; i <= 4; i++)
			v[a[x][i]]++;
		
		f >> x;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				f >> a[i][j];
			
		for (int i = 1; i <= 4; i++)
			v[a[x][i]]++;
		
		for (int i = 1; i <= 16; i++)
			if (v[i] == 2) k++;
		
		if (k >= 2) g << "Case #" << l << ": Bad magician!\n";
		if (k == 0) g << "Case #" << l << ": Volunteer cheated!\n";
		if (k == 1) 
			for (int i = 1; i <= 16; i++)
				if (v[i] == 2) g << "Case #" << l << ": " << i << "\n";
		for (int i = 1; i <= 16; i++)
			v[i] = 0;
		k = 0;
	}
	return 0;
}

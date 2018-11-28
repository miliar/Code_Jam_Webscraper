# include <stdio.h>
# include <algorithm>
# include <iostream>
# include <fstream>


using namespace std;

ofstream fout ("file.out");

int t, n, m, x, o, z;
bool bar[19];

int main ()
{
ios_base::sync_with_stdio(false);
cin.tie(NULL);
	scanf("%d" ,&t);
	
	for (int i = 0; i < t; i++)
	{
		z = 0, o = 0;
		fill(bar, bar+19, 0);
		
		scanf("%d" ,&n);
		for (int h = 1; h <= 4; h++)
			for (int j = 1; j <= 4; j++)
			{
				scanf("%d" ,&x);
				
				if (n==h)	bar[x] = 1;
			}
		
		scanf("%d" ,&m);
		for (int h = 1; h <= 4; h++)
			for (int j = 1; j <= 4; j++)
			{
				scanf("%d" ,&x);
				
				if (m==h && bar[x])	o = x, z++;
			}
			
		fout << "Case #" << i+1 << ": ";
		
		if (z==1)	fout << o << "\n";
		else if (z==0)	fout << "Volunteer cheated!\n";
		else 		fout << "Bad magician!\n";
	}
	
	return 0;
}

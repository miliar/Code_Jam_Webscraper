# include <iostream>
# include <stdio.h>
# include <fstream>
# include <math.h>
# include <algorithm>

using namespace std;
typedef double dl;

FILE *fout = fopen("file2.out", "w");

int T;
dl c, f, x, p, k;

int main ()
{
	cin >> T;
		
	for (int i = 0; i < T; i++)
	{
		cin >> c >> f >> x;
		
		dl mn = (dl)x/2;
		p = 2;
		k = 0;
		
		while(1)
		{
			if (mn > k + ((dl)c/p) + (dl)x/(p+f))
			{
				mn = k + ((dl)c/p) + (dl)x/(p+f);
				k = k + (dl)c/p;
				p += f;
			}
			else
				break;
		}
		
		fprintf(fout, "Case #%d: %.7lf\n" ,i+1,mn);
		
	}
	
	return 0;
}

#include <iostream>

#include <fstream>

using namespace std;

ofstream fout("file.out");

int t,a,b,p,v[20],v1[20];

int main()
{
	cin >> t;
	
	for (int i = 1; i <= t; i++)
	{
		for (int h = 1; h <= 2; h++)
		{
			cin >> a;
			for (int j = 0; j < 4; j++)
				for (int k = 0; k < 4; k++)
				{
					cin >> b;
					if (j+1 == a) v[b]++;
				}
		}
		
		int san = 0,ans;
		for (int j = 1; j <= 16; j++)
		{
			if (v[j] == 2) san++,ans = j;
			v[j] = 0;
		}

		if (san == 1)
			fout << "Case #" << i << ": " << ans << "\n";
		else if (san > 1)
			fout << "Case #" << i << ": Bad magician!\n";
		else
			fout << "Case #" << i << ": Volunteer cheated!\n";
	}
}

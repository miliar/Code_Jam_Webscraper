#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int tab[17];

int main()
{
	int zestaw;
	cin >> zestaw;
	
	for(int mm = 1; mm <= zestaw; mm++)
	{
		for(int i = 1; i <= 16; i++)
			tab[i] = 0;
			
		for(int i = 1; i <= 2; i++)
		{
			int k;
			cin >> k;
			
			for(int m = 1; m <= 4; m++)
			{
				for(int n = 1; n <= 4; n++)
				{
					int a;
					cin >> a;
					
					if(m == k)
						tab[a]++;
				}
			}
		}
		
		bool t = false;
		int w = -1;
		
		for(int i = 1; i <= 16; i++)
		{
			if(tab[i] == 2)
			{
				if(t == false)
				{
					t = true;
					w = i;
				}
				else
				{
					cout << "Case #" << mm << ": Bad magician!" << endl;
					goto A;
				}
			}
		}
		
		if(w != -1)
		{
			cout << "Case #" << mm << ": " << w << endl;
		}
		else
		{
			cout << "Case #" << mm << ": Volunteer cheated!" << endl;
		}
		
		A:;
		
	}

	return 0;
}


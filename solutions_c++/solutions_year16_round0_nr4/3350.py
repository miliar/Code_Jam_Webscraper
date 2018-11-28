#include <iostream>
#include <fstream>

using namespace std;
int main()
{
	//ifstream cin("in.txt");
	//ofstream cout("out.txt");

	int t,K,C,S;
	cin >> t;
	for (int a0 = 1; a0 <= t; a0++)
	{
		cin >> K >> C >> S;
		if (C == 1)
		{	
			if (S < K)
			{	
				cout << "Case #" << a0 << ": " << "IMPOSSIBLE" << endl;
				continue;
			}
			else
			{
				cout << "Case #" << a0 << ": ";
				for (int i=1;i<=K;i++)
					cout << i << " ";
				cout << endl;
				continue;
			}
		}
		else
		{
			if (S < (K + 1) / 2)
				cout << "Case #" << a0 << ": " << "IMPOSSIBLE" << endl;

			else
			{
				int y = K/2;
				int z = 2;
				cout << "Case #" << a0 << ": ";
				while(y--)
				{
					cout << z << " ";
					z += 2 * K + 2;
				}
				if (K % 2 == 1)
					cout << K << endl;
				else
					cout << endl;
			}

		}
	}

return 0;
}
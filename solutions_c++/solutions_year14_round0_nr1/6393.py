#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int T = 0, R1 = 0 , R2 = 0;
	int C = -1;
	int CC = 0;
	int A[16] = {};
	int B[16] = {};
	
	
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ": ";
		C = -1;
		CC = 0;
		cin >>  R1;
		for(int r = 0; r < 4; r++)
		{
			for(int c = 0; c < 4; c++)
			{
				cin >>  A[4 * r + c];
			}
		}
		cin >> R2;
		for(int r = 0; r < 4; r++)
		{
			for(int c = 0; c < 4; c++)
			{
				cin >>  B[4 * r + c];
				if(r + 1 == R2)
				{
					for(int i = 0; i < 4; i++)
					{
						if(B[4 * r + c] == A[4 * (R1 - 1)  + i])
						{
							CC++;
							C = c;
						}
					}
				}
			}
		}
		if(CC == 0)
			cout << "Volunteer cheated!" << endl;
		else if(CC == 1)
			cout << B[4 * (R2-1) + C] << endl;
		else
			cout << "Bad magician!" << endl;
	}
	return 0;
}
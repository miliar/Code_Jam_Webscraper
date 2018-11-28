/* 
	Problem B. New Lottery Game
	George Vafiadis
 */

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
using namespace std;


int main()
{
	int T;

	cin >> T;

	for(int ti = 1; ti <= T; ++ti)
	{
		int A, B, K;

		cin >> A >> B >> K;

		int win = 0;

		for(int a = 0; a < A; ++a)
		{
			for(int b = 0; b < B; ++b)
			{
				if( (a & b) < K)
				{
					++win;
				}
			}	
		}

		cout << "Case #" << ti << ": " << win << endl;
	}	

	return 0;
}
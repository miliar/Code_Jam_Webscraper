#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;


int main()
{
	
		int cases;
		unsigned long long KtoC;
		unsigned long long K, C, S;
		cin >> cases;
		for (int x = 1; x <= cases; x++)
		{
			cin >> K >> C >> S;
			cout << "Case #" << x << ": ";
			if (K > S)
				cout << "IMPOSSIBLE";
			else {
				cout << "1";
				KtoC = pow(K, C-1);
				for (int x = 1; x < K; x++)
				{
					cout << " " << x*KtoC+1;
				}
			}
			cout << endl;			
		}
		return 0;
}


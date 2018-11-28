#include<iostream>
#include<fstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	/*ifstream cin;
	ofstream cout;
	cin.open("fractiles.in");
	cout.open("fractiles.out");*/

    long long int testCases;
	cin >> testCases;

	long long int tc = 0;
    while (++tc <= testCases)
    {
		cout << "Case #" << tc << ": ";

		long long int k, c, s;
		cin >> k >> c >> s;

		if (c == 1)
		{
			if (s < k)
			{
				cout << "IMPOSSIBLE";
			}
			else
			{
				for (int i = 1; i <= k; i++)
				{
					cout << i << " ";
				}
			}
			
			cout << endl;

			continue;
		}

		if (s < k/2 + 1)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			// Partition size.
			long long int psize = pow(k, c - 1);
			long long int currPart = 0;
			for (int i = 1; i <= k; i += 2)
			{
				int checkChar = i;
				if (i + 1 <= k)
				{
					checkChar = i + 1;
				}

				cout << currPart + checkChar << " ";

				currPart += 2 * psize;
			}
		}
		
		cout << endl;
    }

	/*cin.close();
	cout.close();*/
    
    return 0;
}

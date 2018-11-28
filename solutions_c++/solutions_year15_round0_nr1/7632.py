#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
using namespace std;

int main()
{
	ofstream output("output.txt");
	int T = 0;
	
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int friendneeded = 0;
		int standingup = 0;
		int highestshynesslevel = 0;
		int currentshynesslevel = 1;
		string S;

		cin >> highestshynesslevel >> S;

		standingup += (S[0] - '0');
		
		while (1)
		{
			if (standingup < currentshynesslevel)
			{
				standingup++;
				friendneeded++;
			}
			else
			{
				standingup += (S[currentshynesslevel]-'0');
				currentshynesslevel++;
				if (currentshynesslevel > highestshynesslevel)
				{
					break;
				}
			}
		}
		output << "Case #" << i + 1 << ": " << friendneeded << endl;
	}


	return 0;
}

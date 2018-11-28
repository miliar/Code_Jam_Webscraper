#include <iostream>
#include <math.h>
#include <fstream> 

using namespace std;

int main()
{
	ifstream f;
	f.open("1.in");
	ofstream f1;
	f1.open("2.txt");
	int T;
	char string[1001] , string1[1001] ;
	f >> T;
	for (int k = 0; k < T; k++)
	{
		f >> string;
		string1[0] = string[0];
		for (int i = 1; i <= strlen(string); i++)
		{
			if (string[i]>=string1[0])
			{
				for (int j = i; j > 0; j--)
				{
					string1[j] = string1[j - 1];
				}
				string1[0] = string[i];
			}
			else 
			{
				string1[i] = string[i];
			}
		}
		f1 << "Case #" << k + 1 << ": " << string1 << endl;
	}
	system("pause");
}
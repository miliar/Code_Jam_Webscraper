#include <fstream>
//#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

//Used cplusplus.com for information on different types of integers
//and for information on sprintf() and for information on sqrt() and for information
//on limits for floating-point variables

int main(void)
{
	ifstream infile;
	infile.open("C-small-attempt0.in.txt");
	ofstream outfile ("C-small.out");
	int T = 0;
	infile >> T;
	/*char test[4];
	sprintf(test, "%d", 7);
	cout << test << "\n";*/
	for (int i = 0; i < T; i++)
	{
		unsigned long long int start = 0;
		unsigned long long int end = 0;
		infile >> start >> end;
		int count = 0;
		char* num = (char*) malloc(sizeof(char) * 5);
		for (unsigned long long int j = start; j <= end; j++)
		{
			double s = (double) j;
			double rt = sqrt(s);
			unsigned long long int asInt = (int) rt;
			if (rt == (double) asInt)
			{
				sprintf(num, "%d", j);
				int flag = 0;
				int length = strlen(num);
				for (int k = 0; k < length/2; k++)
				{
					if (num[k] != num[length-k-1])
					{
						flag = 1;
						break;
					}
				}
				if (flag == 1)
					continue;
				sprintf(num, "%d", asInt);
				length = strlen(num);
				for (int z = 0; z < length/2; z++)
				{
					if (num[z] != num[length-z-1])
					{
						flag = 1;
						break;
					}
				}
				if (flag == 0)
				{
					count++;
					//cout << j << "\n";
				}
			}
			/*else
			{
				cout << rt << " " << asInt << "\n";
			}*/
		}
		outfile << "Case #" << i+1 << ": " << count << "\n";
	}
	
	infile.close();
	outfile.close();
	
	return 0;
}		
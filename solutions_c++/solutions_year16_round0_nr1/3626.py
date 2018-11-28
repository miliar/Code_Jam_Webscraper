#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;

int checkSleep(int count[]);

int main(void)
{
	ifstream file;
	file.open("A-large.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for (int t = 1; t <= caseNo; t++)
	{
		long int n;
		file >> n;

		if (n == 0)
		{
			output << "Case #" << t << ": ";
			output << "INSOMNIA" << endl;
		}
		else
		{
			int count[10] = { 0 };
			char s[10];
			int multiplier = 1;
			int temp;

			do
			{
				temp = n * multiplier;

				_itoa_s(temp, s, 10);
				for (int tt = 0; tt < 10; tt++)
				{
					if (s[tt] == '\0') break;
					else count[s[tt]-48]++;
				}

				multiplier++;

			} while (checkSleep(count));




			output << "Case #" << t << ": ";
			output << temp << endl;
		}
	}
}

int checkSleep(int count[])
{
	if (count[0] == 0 || count[1] == 0 || count[2] == 0 || count[3] == 0 || count[4] == 0 || count[5] == 0 || count[6] == 0 || count[7] == 0 || count[8] == 0 || count[9] == 0)
		return 1;
	else return 0;
}
#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <string>
using namespace std;

int calInviters(int, string);

void main()
{
	ifstream fin;
	fin.open("file.in");


	ofstream fout;
	fout.open("file.out");

	int n = 0, i = 1;
	fin >> n;

	cout << left << setw(15) << n;

	string audience;
	int sMax;
	int invites;

	while (i <= n)
	{
		fin >> sMax;
		fin >> audience;
		invites = calInviters(sMax, audience);
		cout << "Case #" << i << ": " << invites << endl;
		cout << sMax << " " << left << setw(12) << audience << " ";
		fout << "Case #" << i << ": " << invites << endl;
		i++;
	}
	cout << endl;
	fin.close();
	fout.close();

}

int calInviters(int s, string aud)
{
	int i = 0, countAud = 0, countInvit = 0;
	int x = 0;
	while (i <= s)
	{
		char c = aud[i];
		x = atoi(&c);
		if (aud[i] != '0')
		{
			if (countAud < i)
			{
				countInvit += (i - countAud);
				countAud += countInvit;
			}
			countAud += x;
		}
		i++;
	}
	return countInvit;
}
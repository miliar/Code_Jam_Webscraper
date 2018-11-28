#include <iostream>
#include <fstream>
#include <string>
using namespace std;
void main()
{
	int shy;
	string aud;
	int count;
	int extra;
	int inpt;

	int n;
	ofstream fout("output1.txt");
	ifstream fin("A-large.in");
	fin >> n;
	inpt = 0;
	
	for (int i = 0; i < n; i++)
	{
		extra = 0;
		count = 0;
		fin >> shy;
		fin >> aud;
		for (int j = 0; j <= shy; j++)
		{
			inpt = aud[j] - '0';
			if (count < j)
			{
				extra += j - count;
				count += j - count;
			}
			count += inpt;
			
		}


		fout << "Case #" << i+1 << ": " << extra<<endl;
	}
	fout.close();
	fin.close();
}
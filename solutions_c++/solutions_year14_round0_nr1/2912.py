// CodeJam_QR14_01.cpp : Defines the entry point for the console application.
//

#include <fstream>

#define FIRST 0
#define SECOND 1

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int SmallConst=30,size=4;

void Solve()
{
	int c,hand[size][2],ct=0,cct=-1;	//ct is count, cct is current number
	char temp[SmallConst];

	fin >> c;
	for (int i=0;i<c;i++)
		fin.getline(temp,SmallConst);

	for (int i=0;i<size;i++)
		fin >> hand[i][FIRST];

	for (;c<=size;c++)
		fin.getline(temp,SmallConst);

	fin >> c;
	for (int i=0;i<c;i++)
		fin.getline(temp,SmallConst);

	for (int i=0;i<size;i++)
	{
		fin >> hand[i][SECOND];
		for (int j=0;j<size;j++)
			if (hand[j][FIRST]==hand[i][SECOND])
				cct=hand[j][FIRST],ct++;
	}

	for (;c<=size;c++)
		fin.getline(temp,SmallConst);

	switch (ct)
	{
		case 0:
			fout << "Volunteer cheated!\n";
			break;
		case 1:
			fout << cct << "\n";
			break;
		default:
			fout << "Bad magician!\n";
			break;
	}
}

int main()
{
	int c;
	fin >> c;
	for (int m=1;m<=c;m++)
		fout << "Case #" << m << ": ",Solve();
	return 0;
}


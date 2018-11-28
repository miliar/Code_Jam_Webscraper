#include <cstdlib>
#include <iostream>
#include <math.h>
#include <stack>
#include <fstream>

using namespace std;


void listC(int f, int L[])
{
	for (int num = 0; num < 11; num++)
	{
		if (L[num] == f)
			L[num] = 10;
	}
}

bool listF(int L[])
{
	for (int cum = 0; cum < 11; cum++)
	{
		if (L[cum] != 10)
			return true;
	}
	return false;
}


int main()
{
	ifstream myfile;
	myfile.open("A-large.in");
	ofstream yourfile;
	yourfile.open("asnwerL.out");
	

	int T, N, S, i, Stemp;
	myfile >> T;
	for (int k = 0; k < T; k++)
	{
		myfile >> N;
		i = 0;
		int checkList[11] = { 0,1,2,3,4,5,6,7,8,9,10 };
		bool chk = true;
		while (chk)
		{

			if (N == 0)
			{
				chk = false;
			}
			S = N*(i + 1);
			while (S > 0)
			{
				Stemp = S % 10;
				S = S / 10;
				listC(Stemp, checkList);
				chk = listF(checkList);
			}
			S = N*(i + 1);
			i++;
		}
		if (N>0)
			yourfile << "Case #" << k + 1 << ": " << S << endl;
		else 
			yourfile << "Case #" << k + 1 << ": INSOMNIA" << endl;
	}
	system("pause");
	return 0;
}
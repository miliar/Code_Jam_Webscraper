/* Author: Tran Hua Duc/Dave */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int digCounter(int n, int i, int *digList)
{
	int val = (n * i);

	//val is > 1 digit
	while (val >= 10)
	{
		digList[(val) % 10] = 1;
		val /= 10;
	}

	//val is 1 digit
	digList[val] = 1;

	//Check for existance of digits
	for (int j = 0; j < 10; j++)
	{
		if (digList[j] == 0)
		{
			digList[10] = 0;
			break;
		}
		digList[10] = 1;
	}

	//recurse if digList[10] == 0
	if (digList[10] == 0)
		return digCounter(n, (i + 1), digList);
	else
		return (n * i);
}

int main(int argc, char** argv)
{
	int i, n, t, tres[100000];

	fstream ifile;
	ifile.open("A-large.in", ios::in);
	ifile >> t;

	for (i = 0; i < t; i++)
	{
		int digList[11] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
		ifile >> n;

		if (n == 0)
			tres[i] = -1;
		else
			tres[i] = digCounter(n, 1, digList);
	}
	
	ifile.close();
	ofstream ofile;
	ofile.open("output_l.txt", ios::out);

	for (i = 0; i < t; i++)
	{
		if (tres[i] == -1)
			ofile << "Case #" << i + 1 << ": INSOMNIA" << endl;
		else
			ofile << "Case #" << i + 1 << ": " << tres[i] << endl;
	}

	return 0;
}
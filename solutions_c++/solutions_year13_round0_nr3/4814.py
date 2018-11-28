#include<iostream>
#include<cmath>
#include<fstream>

using namespace std;

int main()
{
	int A, B;
	int lowerLim, upperLim;
	int Tcases;
	int squareNum;
	int sum = 0;
	int n;
	int reverseN;


	ifstream myfile ("test.txt");
	ofstream outfile ("output.txt");

	myfile >> Tcases;

	for (int i = 0; i < Tcases; ++i)
	{
		myfile >> A;
		myfile >> B;
		sum = 0;

		lowerLim = sqrt((double) A);
		if (lowerLim * lowerLim < A)
			++lowerLim;
		upperLim = sqrt( (double) B);

//		cout << "LL: " << lowerLim << endl;
//		cout << "UL: " << upperLim << endl;

		for (int j = lowerLim; j <= upperLim; ++j)
		{
			n = j;
			reverseN = 0;
			while ( n > 0)
			{
				reverseN *= 10;
				reverseN += n%10;
				n /= 10;
			}
			if (j == reverseN)
			{
				squareNum = j*j;
				n = squareNum;
				reverseN = 0;
				while (n > 0)
				{
					reverseN *= 10;
					reverseN += n % 10;
					n /= 10;
				}
				if (squareNum == reverseN)
				{
					sum++;
//					cout << squareNum << endl;
				}
			}
		}
		outfile << "Case #" << (i + 1) << ": " << sum << endl;
	}
	outfile.close();
	myfile.close();
	return 0;
}
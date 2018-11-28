#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include<fstream>
#include <limits>

unsigned long long L, R;
bool test(unsigned long long x)
{
	return ((x >= L) && (x <= R));
}

int main()
{
	std::ofstream outFile;
	outFile.open("a.out");

	std::ifstream inFile;
	inFile.open("a.in");
	/*
	unsigned int x = 10000000;
	for (int i=x; i!=100; --i)
	{
		char buf[21];
		bool bFair = true;
		int n = sprintf(buf, "%d", i);
		for (int j=0; j<n/2; ++j)
		{
			if (buf[j] != buf[n-j-1])
			{
				bFair = false;
				break;
			}
		}
		if (bFair)
		{
			double i2 = i;
			i2 = floor(i2*i2);
			n = sprintf(buf, "%f", i2);
			for (int j=0; j<n; ++j) if (buf[j]=='.') {n = j; break;}
			buf[n] = 0;
			for (int j=0; j<n/2; ++j)
			{
				if (buf[j] != buf[n-j-1])
				{
					bFair = false;
					break;
				}
			}
			if (bFair)
			{
				outFile << buf << std::endl;
			}
		}
	}
	*/

	int NN;
	inFile >> NN;
	//inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int N=1; N<=NN; ++N)
	{
		inFile >> L >> R;
		//inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

		// solution
		int nRes = 0;
		if (test(1)) ++nRes;
		if (test(4)) ++nRes;
		if (test(9)) ++nRes;
		if (test(121)) ++nRes;
		if (test(484)) ++nRes;
		if (test(4004009004004)) ++nRes;
		if (test(4000008000004)) ++nRes;
		if (test(1234567654321)) ++nRes;
		if (test(1232346432321)) ++nRes;
		if (test(1214428244121)) ++nRes;
		if (test(1212225222121)) ++nRes;
		if (test(1210024200121)) ++nRes;
		if (test(1024348434201)) ++nRes;
		if (test(1022325232201)) ++nRes;
		if (test(1020304030201)) ++nRes;
		if (test(1004006004001)) ++nRes;
		if (test(1002003002001)) ++nRes;
		if (test(1000002000001)) ++nRes;
		if (test(40000800004)) ++nRes;
		if (test(12345654321)) ++nRes;
		if (test(12102420121)) ++nRes;
		if (test(10221412201)) ++nRes;
		if (test(10000200001)) ++nRes;
		if (test(404090404)) ++nRes;
		if (test(400080004)) ++nRes;
		if (test(125686521)) ++nRes;
		if (test(123454321)) ++nRes;
		if (test(121242121)) ++nRes;
		if (test(104060401)) ++nRes;
		if (test(102030201)) ++nRes;
		if (test(100020001)) ++nRes;
		if (test(4008004)) ++nRes;
		if (test(1234321)) ++nRes;
		if (test(1002001)) ++nRes;
		if (test(44944)) ++nRes;
		if (test(40804)) ++nRes;
		if (test(14641)) ++nRes;
		if (test(12321)) ++nRes;
		if (test(10201)) ++nRes;

		// output result
		outFile << "Case #" << N << ": " << nRes;
		if (N!=NN) outFile << std::endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}
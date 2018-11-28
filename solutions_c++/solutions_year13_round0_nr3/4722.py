#include <iostream>
#include <fstream>
using namespace std;

double arr[] = {
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004};

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile;
	ofstream outfile;
	infile.open("d:\\testcases1.txt");
	outfile.open("D:\\result1.txt");

	int testcases = 0;
	int count;
	int iterator;
	double lower;
	double upper;

	infile>>testcases;
	
	for (int i=0;i<testcases;i++)
	{
		count = 0;
		lower = 0;
		upper = 0;
		infile>>lower;
		infile>>upper;

		for (iterator = 0; iterator<39;iterator++)
		{
			if (arr[iterator]>=lower && arr[iterator] <= upper)
				count++;
			else if (arr[iterator] > upper)
				break;
		}
		outfile<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	return 0;
}
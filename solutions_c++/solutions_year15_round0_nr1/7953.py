#include"iostream"
#include"fstream"
using namespace std;

int main()
{
	ifstream infile;
	infile.open("D:\\A-large.in");

	ofstream outfile;
	outfile.open("D:\\A-large");

	int t = 0, smax = 0;
	//char a[10];
	char a[1020];
	
	infile >> t;

	for (int i = 0; i < t; i++)
	{
		infile >> smax;
		infile >> a;
		int count = 0, sum = 0;

		sum = a[0] - '0';
		for (int j = 0; j < smax; j++)
		{
			if (j + 1 <= sum)
			{
				sum += a[1 + j] - '0';
			}
			else 
			{
				count += j - sum + 1;
				sum = a[1 + j] - '0' + j + 1;
			}
		}
		outfile << "Case #" << i + 1 << ": " << count << endl; 
	}

	infile.close();
	outfile.close();
	//cin >> t;
	return 0;
}
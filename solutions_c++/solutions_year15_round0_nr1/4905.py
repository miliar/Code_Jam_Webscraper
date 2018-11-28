#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream ifile;
	ifile.open("A-large.in");
	char * aud=nullptr;
	int total;
	int * count=nullptr;
	ifile >>total;
	ofstream ofile;
	ofile.open("output.txt");
	int max;
	int friends;
	aud = new char[1100];
	
	int cur = 0;
	for (size_t i = 0; i < total; i++)
	{
		friends = 0;
		ifile >> max;
		ifile >> aud;
		cur = aud[0] - 48;

		
		for (size_t j = 1; j <= max; j++)
		{
			
			//while (cur < j && aud[j]!='0')
			if (cur < j && aud[j] != '0')
			{
				friends+=(j-cur);
				aud[j] += (j - cur);
			}
		
			cur += aud[j] - 48;
		}

		ofile <<"Case #"<<i+1<<": "<< friends << endl;
	}

	return 0;
}
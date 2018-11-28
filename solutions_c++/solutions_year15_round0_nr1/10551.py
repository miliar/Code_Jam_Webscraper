#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream ifile;
	ifile.open("test.txt");
	int test=0;
	ifile>>test;
	ofstream ofile;
	int friends=0,sum=0,shy_level=0,num=0;
	char chr[1];
	ofile.open("rezult_q1.txt");
	for(int j=0;j<test;j++)
	{
		ifile>>shy_level;
		friends=sum=0;
		for(int i=0;i<=shy_level;i++)
		{
			ifile>>chr[0];
			num=atoi(chr);
			if((sum+friends)<i)
				friends=friends+(i-(sum+friends));
			sum+=num;
		}
		ofile<<"Case #"<<j+1<<": "<<friends<<endl;
	}
	ofile.close();
	ifile.close();
	
	return 0;
}
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <fstream>

using namespace std;

bool ispalindrome(long num)
{
	string str = static_cast<ostringstream*>( &(ostringstream() << num) )->str();
	long len = str.length();
	for(long j = 0 ; j < (len / 2); j++)
	{
		if(str[j] != str[len - 1 -j])
			return false;
	}
	return true;
}

int main(int argc, char *argv[])
{
	ifstream infile;
	string line;
	
	infile.open(argv[1],ios::in);
	if(!infile.is_open())
	{
		cout<<"Unable to open input file\n";
		exit(1);
	}

	// Read the first line containing the number of test cases
	if(!getline(infile,line))
	{
		cout<<"Cannot read the first line containing the number of test cases\n";
		infile.close();
		exit(1);
	}

	int testCasesCount = 0, nTestCases = atoi(line.c_str());
	long lowerlimit,upperlimit, count;
	long double dnum;
	char *pch;
	string slowerlimit, supperlimit;
	ofstream outfile("output.txt",ios::out);
	
	while(getline(infile,line))
	{
		testCasesCount++;
		count = 0;

		stringstream ss(line);
		getline(ss, slowerlimit, ' ');
		getline(ss, supperlimit, ' ');
		lowerlimit = atoi(slowerlimit.c_str());
		upperlimit = atoi(supperlimit.c_str());

		for( ; lowerlimit <= upperlimit ; lowerlimit++)
		{
			dnum = sqrt(lowerlimit);
			if( std::floor(dnum) == dnum && ispalindrome(lowerlimit) && ispalindrome((long)dnum))
				count++;
		}

		outfile<<"Case #"<<testCasesCount<<": "<<count<<endl;
		if(testCasesCount == nTestCases)
			break;
	}
	return 0;
}
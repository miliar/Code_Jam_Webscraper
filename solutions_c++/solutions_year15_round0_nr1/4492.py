// My solution for Google jam problem Problem A. Prima donna
// https://code.google.com/codejam/contest/2442487/dashboard#s=p1
// Jerome

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

const char* inFileName = "A-large.in";
const char* outFileName = "out.txt";

int main()
{
	std::ifstream infile(inFileName);
	std::ofstream outfile(outFileName);
	if( infile.fail() || outfile.fail() )
	{
		return 0;
	}
	
	string line;
	getline(infile,line);
	int T = stoi(line);
	
	for( int Case = 1; Case <= T; Case++ )
	{
		getline(infile,line);
		istringstream iss(line); 
		int S;
		iss >> S;
		string audience;
		iss >> audience;
		
		int nbPublic = 0;
		int added = 0;
		for( int level=0; level< audience.size(); level++ )
		{
			int qtt = audience[level] - '0';

			if( qtt == 0 )
			{
				// pass
			}
			else if( level - nbPublic <= 0 )
			{
				// it's alright
				nbPublic += qtt;
			}
			else
			{
				int temp = level - nbPublic;
				nbPublic += temp + qtt;
				added += temp;
			}
		}

		cout<<"Case #"<<Case<<": "<<added<<endl;
		outfile <<"Case #"<<Case<<": "<<added<<endl;
	}

    infile.close();
	outfile.close();
	system("pause");
	return 0;
}
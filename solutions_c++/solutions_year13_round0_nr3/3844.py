#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <cmath>
#include <string.h>
using namespace std;

int main()
{
	string line;
	int numtc;
	ifstream myfile ("C-small-attempt0.in");
//	ifstream myfile ("input.txt");
	getline (myfile,line);
	numtc = atoi(line.c_str());

	long long start;
	long long end;
	for(int testCaseNum=1; testCaseNum <= numtc; testCaseNum++)
	{
		if (myfile.is_open())
		{
			myfile >> start;
			myfile >> end;
		}

		long count=0;
		long long sq_start;
		long long sq_end;
		if(sqrt(start) == (int)(sqrt(start))) sq_start = sqrt(start);
		else sq_start = sqrt(start) + 1;
		sq_end = sqrt(end);

		stringstream ss;
		string temp;
		for(long long i=sq_start; i<=sq_end; i++)
		{
			ss << i;
			temp = ss.str();
			if (temp == string(temp.rbegin(), temp.rend()))
			{
				ss.str("");
				ss << (i*i);
				temp = ss.str();

				if (temp == string(temp.rbegin(), temp.rend()))
					count++;
//				cout << "fair n square!! " << i*i <<endl;
			}
			ss.str("");
		}

		cout << "Case #" << testCaseNum << ": " << count << endl;
	}
	myfile.close();
	return 0;
}

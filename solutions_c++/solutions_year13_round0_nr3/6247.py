#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <sstream>

using namespace std;

string numtostr(int num);

bool pal(int num)
{
	string str = numtostr(num);
	
	int half = (str.length() + 1) / 2;
	
	int limit = str.length() - 1;
	
	for (int i = 0; i < half; i++)
	{
		if (str[i] != str[limit - i])
			return false;
	}
	return true;
}

bool fairsqr(int num)
{
	double tmp = sqrt(num);
	double intpart;
	if (modf(tmp, &intpart) == 0)
	{
		if ( pal(num) && pal( tmp ) )
			return true;
	}
	return false;
}

int main(int argc, char **argv)
{
	if (argc != 3)
	{
		cout << "Invalid number of arguments" << endl;
		return 0;
	}
	
	ifstream infile(argv[1]);
	ofstream outfile(argv[2]);
	
	string in;
	int T, A, B;
	int count;
	
	if (infile.is_open())
	{
		infile >> in;
		T = atoi(in.c_str());
		
		for (int k = 1; k <= T; k++)
		{
			count = 0;
			infile >> in;
			A = atoi(in.c_str());
			infile >> in;
			B = atoi(in.c_str());
			
			for (int i = A; i <= B; i++)
			{
				if ( fairsqr(i) )
					count++;
			}
			
			outfile << "Case #" << k << ": " << count <<endl;
		}
		
		infile.close();
		outfile.close();
	}
	else cout << "Unable to open file" << endl;
	
	return 0;
}

string numtostr(int num)
{
	stringstream ss;
	ss << num;
	string str = ss.str();
	return str;
}

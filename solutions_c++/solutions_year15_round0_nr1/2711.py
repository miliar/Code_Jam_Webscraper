#include <iostream>
#include <fstream>
//#include <vector>
//#include <string>
//#include <cstdlib>
#include <unordered_map>
using namespace std;

int main()
{
	fstream  infile, outfile;
	infile.open("A-large.in", ios::in);
	
	infile.seekg(0, ios::end);  
	if (infile.tellg() == 0) return 0;
	infile.seekg(0, ios::beg);
	
	outfile.open("output.txt", ios::out | ios::trunc);
	int i, j, nCase, sum, num_extra, smax;
	string s;
	infile >> nCase;
	//cout << nCase << endl;
	for(i = 0; i < nCase; i++)
	{
		infile >> smax;
		infile >> s;
		sum = 0;
		num_extra = 0;
		for(j = 0; j <= smax; j++)
		{
			if(s[j] > '0' && sum < j)
			{
				num_extra += j-sum;
				sum = j + (int)(s[j]-'0');
			}
			else
				sum += (int)(s[j]-'0');
				
		}
		outfile << "Case #" << i+1 << ": " << num_extra << endl;
	}
	
	infile.close();
	outfile.close();
	
	return 0;
}

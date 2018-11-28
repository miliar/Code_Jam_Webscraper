#include <iostream>
#include <fstream>
//#include <queue>
#include <vector>
//#include <string>
//#include <cstdlib>
//#include <unordered_map>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
	fstream  infile, outfile;
	infile.open("B-small-attempt1.in", ios::in);
	//infile.open("input.txt", ios::in);
	
	infile.seekg(0, ios::end);  
	if (infile.tellg() == 0) return 0;
	infile.seekg(0, ios::beg);
	
	outfile.open("output.txt", ios::out | ios::trunc);
	
	int i, j, nCase, sum, D, Pi, num1, len1, num2, len2, num3, len3, maxnum;
	
	
	infile >> nCase;
	//cout << nCase << endl;
	for(i = 0; i < nCase; i++)
	{
		infile >> D;
		sum = 0;
		maxnum = INT_MIN;
		vector<int> p;
		for(j = 0; j < D; j++)
		{
			infile >> Pi;
			p.push_back(Pi);
			sum += Pi;
			maxnum = (Pi > maxnum) ? Pi:maxnum;
			//cout << Pi << " ";
		}
		
		len1 = (int)sqrt(sum);
		num1 = 0;
		for(j = 0; j < D; j++)
		{
			if(ceil((double)(p[j])/len1) == 1) continue;
			else num1 += ceil((double)(p[j])/len1) - 1;
		}
		num1 += len1;
		
		len2 = (int)sqrt(sum)+1;
		num2 = 0;
		for(j = 0; j < D; j++)
		{
			if(ceil((double)(p[j])/len2) == 1) continue;
			else num2 += ceil((double)(p[j])/len2) - 1;
		}
		num2 += len2;
		

		len3 = (int)sqrt(sum)-1;
		if(len3 > 0)
		{
			num3 = 0;
			for(j = 0; j < D; j++)
			{
				if(ceil((double)(p[j])/len3) == 1) continue;
				else num3 += ceil((double)(p[j])/len3) - 1;
			}
			num3 += len3;
		}
		else num3 = INT_MAX;	
		
		//cout << " -> " << min( min(num1, num2), maxnum) << endl;
		outfile << "Case #" << i+1 << ": " << min( min(num1, num2), min(num3, maxnum) ) << endl;
	}
	
	infile.close();
	outfile.close();
	
	return 0;
}

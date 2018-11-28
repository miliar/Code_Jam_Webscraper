#include <iostream>
#include <string>
#include <cmath>
#include <cstdio>
using namespace std;

const long int MAXTOP = pow(2,40);

bool isContained (int r[4], int a)
{
	for (int i = 0; i < 4; i++)
	{
		if (r[i] == a)
			return true;
	}
	return false;
}

int main (void)
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		string fractstr;
		cin >> fractstr;
		int P,Q;
		sscanf(fractstr.c_str(),"%i/%i", &P, &Q);
		
		bool possible = false;
		
		cout << "Case #" << (t+1) << ": ";
		
		for (int i = 0; i <= 40; i++)
		{			
			//cout << "h";
			double pd = P * (MAXTOP/(double)Q);
			if (pd != floor(pd))
				continue;
				
			long int p = (long int)pd;
			
			//#nodes on this level
			long int levelSize = pow(2, i);
			long int topSize = pow(2, 40-i);	
			
			//top level ancestors remaining if one node on level is 1/1 elf
			p -= topSize;
			
			
			if (p < 0)
				continue;
			
			//top level ancestors remaining
			long int top = topSize * (levelSize-1);
			
			if (p <= top)
			{
				possible = true;
				cout << i << endl;
				break;
			}
		}
		
		if (!possible)
			cout << "impossible" << endl;
	}
}

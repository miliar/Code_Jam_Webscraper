// CJR1_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <string>
#define ull unsigned long long int
using namespace std;

int main()
{
	fstream fsin("C:\\Users\\basu_lucifer\\Downloads\\A-large (1).in", ios::in), fsout("C:\\Users\\basu_lucifer\\Downloads\\output.out", ios::out | ios::trunc);
	int N;
	ull r,t;
	fsin >> N;
	for(int ts = 1; ts <=N; ++ts)
	{
		fsin >> r >> t;
		ull low = 1, high = t;

		while(low < high)
		{
			ull mid = low + (high-low)/2;
			ull val = (2*(r+mid)-1);
			if((t/mid) < val)
				high = mid;
			else
				low = mid+1;
		}
		fsout <<"Case #" << ts << ": " <<  low - 1 << endl;  
	}
	fsin.close();
	fsout.close();
	return 0;
}




#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main ()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	
	long long T = 0;
	cin >> T;
	long i = 1;
	
	for (i = 1; i<=T; ++i)
	{
		int a[16] = {0};
		int k;
		int tmp;
		cin >> k;
		for (int j=0; j<4; ++j)
		{
			for (int jj=0; jj<4; ++jj)
			{
				cin >> tmp;
				if (j == k-1)
				{
					a[tmp-1]++;
				}
			}			
		}
		cin >> k;
		for (int j=0; j<4; ++j)
		{
			for (int jj=0; jj<4; ++jj)
			{
				cin >> tmp;
				if (j == k-1)
				{
					a[tmp-1]++;
				}
			}			
		}
		
		int q = 0;
		int mx = 0;
		for (int j = 0; j<16; ++j)
		{
			//cout << a[j] << " ";
			if (a[j] > 1) 
			{
				++q;
				mx = j+1;
			}
		}
		
		/*
		Case #1: 7
		Case #2: Bad magician!
		Case #3: Volunteer cheated!
		*/
		if (q == 1)
		{
			cout << "Case #" << i << ": "<<mx;
		}
		if (q == 0)
		{
			cout << "Case #" << i << ": "<<"Volunteer cheated!";
		}
		if (q > 1)
		{
			cout << "Case #" << i << ": "<<"Bad magician!";
		}
		if (i != T) cout << endl;	
	}
	
	
}


// CJ1_LM.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#define lli long long int
using namespace std;

int main()
{
	fstream fsin("C:\\Users\\basu_lucifer\\Downloads\\A-large (2).in", ios::in), fsout("C:\\Users\\basu_lucifer\\Downloads\\output.out", ios::out | ios::trunc);
	int t, n; 
	lli count;
	string s;
	fsin >> t;
	for(int ts = 1; ts <=t; ++ts)
	{
		count = 0;
		fsin >> s >> n;
		int sz = s.length();
		vector<int> v;
		int r = 0;
		
		for(int k = 0; k < sz; ++k)
		{	
			if(s[k] == 'a' || s[k] == 'e' || s[k] == 'i' || s[k] == 'o' || s[k] == 'u')
				r = 0;
			else if((++r) >=n)
				v.push_back(k);
		}
		vector<int>::iterator it;
		if(!v.empty())
		{
			for(int i = 0; i < sz; ++i)
			{
				it = lower_bound(v.begin(), v.end(), i + n-1);
				if(it != v.end())
				{
					count += (sz - *it);
				}
			}
		}
		fsout <<"Case #" << ts << ": " << count << endl;  
	}
	fsin.close();
	fsout.close();
	return 0;
}





#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>

using namespace std;


int main() {
    int t;
	cin>> t;
	for(int i=1; i<=t; i++)
	{
		string s;
		cin >> s;
		
		int n=1;
		char start=s.at(0);
		char prev=start;
		
		int len= s.size();
		for(int j=1; j< len; j++)
		{
			if(s.at(j)!=prev)
			{
				prev=((prev=='+')?'-':'+');
				n++;
			}
		}
		int res;
		if(start=='+')
		{
			if(n%2==0)
				res=n;
			else
				res=n-1;
		}
		else
		{
			if(n%2==0)
				res=n-1;
			else
				res=n;
		}
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}

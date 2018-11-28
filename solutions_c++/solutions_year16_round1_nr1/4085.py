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
		
		int len= s.size();
		string result=s.substr(0,1);
		for(int j=1; j< len; j++)
		{
			if(s.at(j)<s.at(j-1) || s.at(j)<result.at(0))
				result = result+s.substr(j,1);
			else
				result = s.substr(j,1)+result;
		}
		
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}

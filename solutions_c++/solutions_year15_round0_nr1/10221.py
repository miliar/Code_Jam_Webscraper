#include <iostream>
#include <stdio.h>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	int t;
	ifstream in("A-small-attempt2.in");
	ofstream out("output.txt");
	in >> t;
	for(int i=1;i<=t;i++)
	{
		string s;
		int max;
		in >> max >> s;
		int sum=0,cnt=0,len=s.length();
		sum += (s[0]-'0');
		for(int j=1;j<len;j++)
		{
			if(s[j]>'0' && j>sum)
				sum += cnt+= j-sum;
			sum += (s[j]-'0');
		}
		out << "Case #" << i <<": " << cnt;
		if(i!=t)
			out << endl;
	}
	return 0;
}

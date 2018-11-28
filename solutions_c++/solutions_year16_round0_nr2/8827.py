#include <iostream>
#include <fstream>
using namespace std;

int main() {
	// your code goes here
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int T,i,count,len;
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		string s;
		fin>>s;
		count=0;
		len=s.length();
		
		
		for(i=1;i<len;i++)
		{
			if(s[i]!=s[i-1])
			count++;
		}
		if(s[len-1]=='-')
		count++;
		fout<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}

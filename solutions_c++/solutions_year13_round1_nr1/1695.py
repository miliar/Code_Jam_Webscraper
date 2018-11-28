#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<algorithm> 
#include<string>
#include<vector>
using namespace std;
int main()
{
int inc=1;
	ifstream file("i2.in");
	ofstream file2("o1.txt",ios::trunc);
	string s1;
	getline(file,s1);
	int t=atoi(s1.c_str());
	
	for(int x=1;x<=t;x++)
	{
		
		file2<<"Case #"<<inc++<<": ";
		getline(file,s1,' ');
		long long r=atoi(s1.c_str());
		
		getline(file,s1);
		long long t=atoi(s1.c_str());
		long long c=0;
		long int s=0;
		
		while(c<t||c==t)
		{
			c=c+(2*r+1);
			r=r+2;
			s++;
		}
		s--;
		
	    
	    
		file2<<s;
		
		file2<<endl;
	}
}

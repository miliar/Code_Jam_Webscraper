#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	string line,subStr;
	int count=0;
	ifstream infile("test1small");
	double r=0.0,t=0.0;
	string::size_type pos1=0,pos2=0;
	if(!infile)		
		return -1;
	getline(infile,line);
	count=atoi(line.c_str());
	for (int i=0; i<count; ++i)
	{
		getline(infile,line);
		
		pos2=line.find(' ',pos1);

		subStr=line.substr(pos1, pos2 - pos1);
		r=strtod(subStr.c_str(),NULL);
		pos1 = pos2 + 1;
		subStr=line.substr(pos1);
		t=strtod(subStr.c_str(),NULL);
		//cout<<r<<endl<<t<<endl;
		
		double va=floor((sqrt((2*r+3)*(2*r+3)+8*t-16*r-8)-2*r-3.0)/4.0);
		
		long long v=(long long)va;
		//cout<<"va:"<<va<<"v:"<<v<<endl;
		long long temp1=2*(v+1)*(v+(long long)r)+v+1;
		long long temp2=2*(v+2)*(v+1+(long long)r)+v+2;
		if (temp1 <= t && temp2>t)
			cout<<"Case #"<<i+1<<": "<<v+1<<endl;
		else if (temp1 <= t && temp2<=t)
			cout<<"Case #"<<i+1<<": "<<v+2<<endl;
		else if (temp1 > t)
			cout<<"Case #"<<i+1<<": "<<v<<endl;
			
		pos1=0;pos2=0;
	}
}


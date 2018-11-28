#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>
#include <cmath>

using namespace std;

bool checkP(long long a);
//bool checkS(long long a);


bool checkP(long long a)
{
	bool flag=true;
	vector<int> v;
	while(a/10)
	{
		v.push_back(a%10);
		a /=10;
	}
	v.push_back(a);
	for (vector<int>::size_type i=0; i!=v.size(); ++i)
		if (v.at(i)!=v.at(v.size()-1-i))
		{	
			flag=false;
			break;
		}
	return flag;		
}

int main()
{
	bool state=false;
	string line,subStr;
	int count=0,num=0;
	long long A=0, B=0, a=0, b=0;
	string::size_type pos1=0,pos2=0;
	ifstream infile("testcase3",ios::binary | ios::in);
	if(!infile)		
		return -1;
	getline(infile,line);
	count=atoi(line.c_str());
	
	for (int i=0; i<count; ++i)
	{
		getline(infile,line);		
		pos2=line.find(' ',pos1);
		subStr=line.substr(pos1, pos2 - pos1);
		A=atoll(subStr.c_str());
		pos1 = pos2 + 1;
		subStr=line.substr(pos1);
		B=atoll(subStr.c_str());
		pos1=0;
		pos2=0;
		a=(long long)sqrt(A);
		b=(long long)sqrt(B);
		for (long long j=a; j<=b; ++j)
		{
			state=checkP(j);
			if (state && (j*j)>=A)
			{
				if (checkP(j*j))
				{	num++;
				//cout<<j<<", "<<j*j<<endl;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<num<<endl;
		num=0;
	}
	
	return 0;
/* 	line="1010104699876654";
	A=atoll(line.c_str());
	cout<<A<<endl;
	A=(long long)sqrt(A);
	cout<<A<<endl; */
}


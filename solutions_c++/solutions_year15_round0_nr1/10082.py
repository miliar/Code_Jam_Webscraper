#include<iostream>
#include<string>
#include<fstream>
#include<cstring>
#define MAX 10
using namespace std;


int main(int argc, char** argv)
{
	char line[MAX];
	string s;
	int glob=1;
	ofstream myfile(argv[2]);
	ifstream qfile(argv[1]);
	if(qfile.is_open() && myfile.is_open())
	{
		getline(qfile,s);
		while(qfile.getline(line,MAX,'\n'))
		{
			if(strlen(line)==0)
				break;
			int max=line[0]-'0'+2,count=0,extra=0;
			for(int i=2;i<max;i++)
			{
				count+=line[i]-'0';
				if(count>=line[0]-'0')
					break;
				if(count<i-1)
				{
					extra+=(i-1-count);
					count+=(i-1-count);
				}
			}
			myfile<<"Case #"<<glob<<": "<<extra<<"\n";
			glob++;
		}
	}
	return 0;
}

#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
	int t;	
	fstream fin("input1.in",ios::in);
	fstream fout("output.txt",ios::out);
	fin>>t;
	for(int i=0;i<t;i++)
	{
		int s;
		fin>>s;
		string str;
		fin>>str;
		int count=str[0]-48,add=0;
		for(int j=1;j<=s;j++)
		{
			if(count>=j)
				count+=str[j]-48;
			else if(str[j]-48>0)
			{
				add+=j-count;
				count+=str[j]-48+add;
			}
		}
		fout<<"Case #"<<i+1<<": "<<add<<endl;
	}
}

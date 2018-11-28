#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int a;
	fin>>a;
	for(int i=0;i<a;i++)
	{
		string s;
		fin>>s;
			int max=0;
		int num=0;
		int at=0;
		while(true)
		{
		//	char a='+',b='-';
			
	num=0;
	for(int j=0;j<s.length();j++)
		{
			if(s[j]!='-')
			num++;
		}
		if(num==s.length())
		{
			fout<<"Case #"<<i+1<<": "<<at<<endl;
			break;
		}
		for(int j=0;j<s.length();j++)
		{
			if(s[j]=='-')
			max=j;
		}
		for(int j=0;j<=max;j++)
		{
			if(s[j]=='+')
			{
				s[j]='-';
			}
			else
			{
				s[j]='+';
			}
		}
		at++;
		}
		
	}
}

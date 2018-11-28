#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
 
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t,test,len,key,sum;
	string s;
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in",ios::in);
	fout.open("output.txt",ios::out);
	fin>>t;
	test=t;
	while(t--)
	{
	sum=0;
		fin>>s;
		len=s.length();
		key=-1;
		if(len==1 && s[0]=='-')
		{
		sum=1;
		}
		else
		{
		while(key==-1)
	{
		key=1;
		for(int i=1;i<len;i++)
		{
			if(s[0]=='+')
			{
				if(s[i]=='-')
				{
					key=-1;
					sum++;
					for(int j=0;j<i;j++)
					{
					s[j]='-';
					}
					break;
				}
				else
				{
				key=1;
				}
			}
			else
			{
				if(s[i]=='+')
				{
					key=-1;
					sum++;
					for(int j=0;j<i;j++)
					{
					s[j]='+';
					}
					break;
				}
				else
				key=1;
			}
		}
		}
	}
	if(s[0]=='-' && len!=1)
	sum++;
	fout<<"Case #"<<test-t<<": "<<sum<<"\n";
	}
		fin.close();
	fout.close();
return 0;	
}
 

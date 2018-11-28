#include<bits/stdc++.h>
using namespace std;

int main()
{
	fstream fin("B-large.in",ios::in);
	fstream fout("outp.txt",ios::out);
	int t;
	fin>>t;
	for(int i=0;i<t;i++)
	{
		char s[101];
		fin>>s;
		int count=0;
		if(s[0]=='-')
			count=-1;
		int check=0;
		for(int j=0;j<strlen(s);j++)
		{
			if(s[j]=='-' && check==0)
			{
				check=1;
			}
			else if(s[j]=='+' && check==1)
			{
				count+=2;
				check=0;
			}
		}
		if(check==1)
			count+=2;
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}

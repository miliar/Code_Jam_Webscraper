#include<iostream>
#include<fstream>
using namespace std;



bool grt(string str1, string str2)
{
	int flag=0;
	for(int i=0;i<str1.length();i++)
	{
		if(str2[0]>=str1[i])
		flag++;
	}
	if(flag==str1.length())
	return true;
	else
	return false;
	
	
}


int main()
{
	
	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);
	
	int i,t;
	fin>>t;
	for(i=1;i<=t;i++)
	{
		string str,str1="",str2="";
		fin>>str;
		int j;
		for(j=0;j<str.length();j++)
		{
			string temp;
			temp=str[j];
			if(grt(str1,temp))
			{
				str2=str[j]+str1;
			}
			else
			{
				str2=str1+str[j];
			}
			str1=str2;
		}
		
		
		fout<<"Case #"<<i<<": "<<str1<<endl;
	}
	
	
	cout<<"done";
	return 0;
}


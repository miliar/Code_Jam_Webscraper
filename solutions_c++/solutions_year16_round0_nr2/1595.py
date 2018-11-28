#include<iostream>
#include<fstream>
using namespace std;

string str;

bool check()
{
	for(int i=0;i<str.length();i++)
	{
		if(str[i]=='-')
		return false;
	}
	
	return true;
}


void rev(int a)
{
	string temp="";
	temp=str;
	for(int i=0;i<a;i++)
	{
		if(str[i]=='-')
		temp[a-1-i]='+';
		else
		temp[a-1-i]='-';
	}
	str=temp;
}

int algo()
{
	int a=0,i;
	if(str[0]=='-')
	{
		for(i=str.length();i>0;i--)
		{
			if(str[i-1]=='-')
			break;
		}
		rev(i);
		a++;
	}
	else
	{
		for(i=0;i<str.length();i++)
		{
			if(str[i]=='-')
			break;
		}
		rev(i);
		a++;
	}
	return a;	
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
		str="";
		fin>>str;
		int j=0;
		
		while(j<200)
		{
			if(check())
			break;
			j=j+algo();
		}
		fout<<"Case #"<<i<<": "<<j<<endl;
	}
	cout<<"done";
	return 0;
}

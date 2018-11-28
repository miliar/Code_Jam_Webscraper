#include <iostream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;
void find(string s, long long int test)
{
	ofstream outfile;	
	outfile.open("bout.txt", std::ios_base::app);
	long long int len = s.length();
	//cout<<s<<endl;
	//cout<<len<<endl;
	long long int ans=0,flag=1;
	for(long long int i=len-1;i>=0;i--)
	{
		//cout<<s[i];
		if(s[i]=='+' && flag == 1)
		{
			flag=1;
		}
		else if(s[i]=='-' && flag == 1)
		{
			flag=2;
			ans++;
		}
		else if(s[i]=='-' && flag == 2)
		{
			flag=2;
		}
		else if(s[i]=='+' && flag == 2)
		{
			ans++;
			flag=1;
		}
	}
	
	outfile << "Case #"<<test<<": "<<ans<< endl;
	outfile.close();
}

int main()
{
	long long int test, i=1;
	///*
	ifstream myfile ("B.txt");
	if (myfile.is_open())
  	{
  		myfile >> test;
  		string s;
  		while ( myfile >> s )
	    {
	    	find(s,i);
	    	i=i+1;
	    }
	    myfile.close();
  	}
	return 0;
}
#include <iostream>
#include <fstream>
#include<cstdio>
using namespace std;

int main() {
	// your code goes here
	ifstream in;
	ofstream of;
	in.open("input.txt");
	of.open("output.txt");
	int t,i;
	in>>t;
   for(i=0;i<t;i++)
	{
	string s;
	in>>s;
	int count,j,flag;
	count=0;
	if(s[0]=='+')
	flag=1;
	else
	flag=0;
	for(j=1;j<s.size();j++)
	  {
	      
	      if(s[j]=='+'&&flag==1)
	      {
	          
	          
	      }
	      else if(s[j]=='+'&&flag==0)
	      {
	          count++;
	          flag=1;
	      }
	        else if(s[j]=='-'&&flag==0)
	      {
	          
	      }
	        else if(s[j]=='-'&&flag==1)
	      {
	          count++;
	          flag=0;
	      }
	  }
	  if(flag==0)
	  count++;
	of<<"Case #"<<(i+1)<<": "<<count<<"\n";
	}
	return 0;
}


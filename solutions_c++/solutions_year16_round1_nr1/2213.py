#include<algorithm>
#include<stack>
#include<deque>
#include<string>
#include<vector>
#include<string.h>
#include<iostream>
#include<fstream>
#include<ctype.h>
#include<math.h>
#include<memory>
#include<climits>
using namespace std;
int main()
{
  int test;
	ifstream fi("A-large.in",ios::in);
	ofstream fo("A-large.out",ios::out);
	
	fi>>test;
	deque<char> md;
	char str[2000];
	fi.getline(str,2000,'\n');
	for(int i=0;i<test;i++)
	{
	
	  fi.getline(str,2000,'\n');
	   
	  for(int j=0;j<strlen(str);j++)
	  {
	  	if(j==0)
	  	{
		   md.push_front(str[j]);
		   continue;
	    }
	  	 
	  	 if(str[j]<=md.front() )
	  	{
	  		md.push_front(str[j]);
	  	}
	  	else if(str[j]>=md.back())
	  	{
	  		md.push_back(str[j]);
	  	}
	  	else
	  	{
	  		md.push_front(str[j]);
	  	}
	  }
	
	fo<<"Case #"<<i+1<<":"<<" ";
	
     while (!md.empty())
       {
        fo<< md.back();
         md.pop_back();
        }
        
        fo<<"\n";
        memset(str,0,strlen(str));
    }
return 0;
}
	
	
	




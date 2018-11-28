#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
int main()
{
	int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	string s1,sa,sb;
	stringstream si,sf;
	getline(file,s1);
	while(!file.eof())
	{
		getline(file,sa,' ');
		unsigned long long a=atoi(sa.c_str());
		getline(file,sb);
		unsigned long long b=atoi(sb.c_str());
		unsigned long long z;
		int count=0;
		
		for(z=a;z<=b;z++)
		{
	      unsigned long long r=sqrt(z);
		  if(z==(r*r))
		  {
		  
		  	int ans=0;
		  	si<<z;
		  	s1=si.str();
		  	si.str("");
		  	si.clear();
		  	int l=strlen(s1.c_str());
		  
		  	for(int y=0;y<l;y++)
		  	{
		  		if(s1[l-y-1]!=s1[y])
		  		{
		  		
		  			ans=-1;
		  			break;
		  		}
		  	}
		  	if(ans==0)
		  	{
		  
		  		int ans2=0;
		  		sf<<r;
		  		s1=sf.str();
		  		sf.str("");
		  	    sf.clear();
		  	int l=strlen(s1.c_str());
		  	for(int y=0;y<l;y++)
		  	{
		  		if(s1[l-y-1]!=s1[y])
		  		{
		  			ans2=-1;
		  			break;
		  		}
		  	}
		  	if(ans2==0)
		  	{
		  		count++;
		  	}
		  	}
		  }  
	    }
	    
	    
	    
		file2<<"Case #"<<inc++<<": ";
		file2<<count;
		file2<<endl;
	}
}

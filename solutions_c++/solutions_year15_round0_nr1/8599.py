#include<iostream>
#include <fstream>
#include <string>
#include<stdlib.h>
#include<conio.h>
#include<iomanip>
using namespace std;



int main()
{
  ifstream myfile ("A-large.in");
  ofstream ofile ("xyz.out");
  
    
    
  
  
  if (myfile.is_open() || ofile.is_open())
  {
   long long int T;
myfile>>T;
for(long long int i=1;i<=T;i++)
{long long int count=0,z=0,max,m=0;
string s;
myfile>>max;
myfile>>s;
long long int a=s.at(0);
z=a-48;

if(max==0)
{
ofile<<"Case #"<<i<<": "<<0<<endl;}
else
{
for(long long int j=1;j<s.length();j++)
{long long int x=s.at(j);
long long int y=x-48;
if(z<j)
{long long int f=j-z;
count=count+f;
z=z+y+f;

}
else
{z=z+y;
}
}
ofile<<"Case #"<<i<<": "<<count<<endl;
}
}

 myfile.close();
ofile.close();
  }

	return 0;
}


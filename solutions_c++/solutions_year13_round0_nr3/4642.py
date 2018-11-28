#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <cmath>
using namespace std;
string change (double num )
{
string Result;          // string which will contain the result

ostringstream convert;   // stream used for the conversion

convert << num;      // insert the textual representation of 'Number' in the characters in the stream

Result = convert.str(); 
return Result;
}
bool check (string s)
{ int num=s.length()/2;
 for(int i=0;i<num;i++)
 { if(s[i]!=s[s.length()-1-i])
     return false;
 }
 
 return true;
}
int main ()
{ 
  ifstream fin ("input.txt");
  ofstream fout ("google1.txt");
int n;
double a,b;
double num =0;
string s1,s2;
fin>>n;
for(int i=0;i<n;i++)
{
	fin>>a>>b;
	num=0;
	for(double i=a;i<=b;i++)
	{
		s1=change(i);
	    if(check(s1))
		{
        s2=change(sqrt(i));  	
	    if(check(s2)) 
			num++;
		}
	}
	fout<<"Case #"<<i+1<<": "<<num<<endl;
 

}return 0;
}
#include<iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

std::ifstream infile("thefile5.in");
class opera
{
int Smax,A[7],num;
public:
	void read();
	void function();
	void display(int);
};
void opera::display(int x)
{

cout<<"Case #"<<x+1<<": "<<num<<endl;
}
void opera::read()
{
 string intAsString;
infile>>Smax;
infile>>intAsString;
int asInt = 0;
stringstream ss;
     ss<<intAsString;
     ss>>asInt; 
     ss.str(""); 
     ss.clear();
     

for(int i=Smax;i>=0;i--)
	 {
	 A[i]=asInt%10;
	 asInt=asInt/10;
	 }
}
void opera::function()
{
int clap=0;
if(A[0]>0)
 clap=A[0];
 num=0;
 
 for(int k=1;k<Smax+1;k++)
 	{
 	if(k<=clap)
 	clap+=A[k];
 	
 	else
 	{
 	int loop=k-clap;
 	num+=loop;
 	clap=clap+loop+A[k];
 	}
 	
 	

 	}
 }	
int main()
{
int T;
opera o[101];

infile>>T;

for(int i=0;i<T;i++)
{
o[i].read();
o[i].function();
}
for(int i=0;i<T;i++)
o[i].display(i);
}


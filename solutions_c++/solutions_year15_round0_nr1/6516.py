#include<iostream>
#include <fstream>
#include<string.h>
using namespace std;
int main()
{
ifstream in("A-large.in");   //enter file name here
	ofstream out("A-large2.out");            //output file
 int Smax=0,invited=0;
 int testnum=0;
 in>>testnum;
 int counter=0;
  int innercounter=0;
 int sum=0;
 int temp=0;
char arg[1020]; 
while(counter<testnum)
{innercounter=1;
invited=0;
temp=0;
sum=0;
    in >> Smax;

	in >>arg;
	sum=arg[0]-48;
	while(innercounter<Smax+1)
		{
			if(innercounter>sum)
		{
			
         invited+=innercounter-sum;
		 sum+=innercounter-sum;
         
		}
			temp=arg[innercounter]-48;	//in>>temp;
			sum+=temp;
		innercounter++;		
		}
	out<<"Case #"<<counter+1<<": "<<invited<<endl;
	
	counter++;
	
}

	
return 0;
}
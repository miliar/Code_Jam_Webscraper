#include<iostream>
#include<conio.h>
#include<fstream>
#include<stdlib.h>
using namespace std;
int main(void)
{
	
ifstream in;
ofstream out;
in.open("A-large.in");
out.open("out1.txt");

string t;
getline(in,t);
long d=atoi(t.c_str());

for(long j=1;j<=d;j++)
 {
     string num;
     in>>num;
	 long n=atoi(num.c_str());
	 if(n==0)
	 {
	 	out<<"Case #"<<j<<": INSOMNIA"<<endl;
	 }
	 else
	{  
	   long p,q;
	   int i,ar[10],check=0,z=1;
	   for(i=0;i<10;i++)
	        ar[i]=0;
	
	 	while(check==0)
	 	{
	 		p=n*z;
	 		q=p;
	 		z+=1;
	 		while(p!=0)
	 		{ 
	 	    	ar[p%10]=1;
	 	    	p/=10;
	 	    }
	 	    check=1;
	 	    for(i=0;i<10;i++)
	 	    {  
	 	    	if(ar[i]==0)
	 	    	{
	 	    		check=0;
	 	    		break;
				 }
			 }
	 			
		 }
		 out<<"Case #"<<j<<": "<<q<<endl;
		 
	 }
	 
	 
 }

 
 
in.close();
out.close();
getch();
}

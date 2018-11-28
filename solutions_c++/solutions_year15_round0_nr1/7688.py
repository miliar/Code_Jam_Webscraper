#include<iostream>
#include <fstream>
using namespace std;
int main ()
{
	ifstream in ( "A-large.in");
	ofstream out ("output.txt");
	int tcase;
	in>>tcase;
	int smax;
	int r,ad;
    string s;
    int sum;
    int h;
	for( int i=1;i<=tcase;i++)
	{
	r=0;
	ad=0;
	sum=0;
		in>>smax;
		in>>s;
		
		
	for (int i=0;i<=smax;i++)
	{
	h= s[i]-'0';
		if(h!=0)
		{
			if(sum<i)
		   {
		   	
			ad=i-sum;
			r+=ad;
			sum =sum+ad+h;
		   }
		   else 
		   
	 	sum =sum+h;
		
		
			
		}
		
		
	}
		
		
		
	out<<"Case #"<<i<<": "<<r<<endl;	
		
	}//tcase
	
	
}//main

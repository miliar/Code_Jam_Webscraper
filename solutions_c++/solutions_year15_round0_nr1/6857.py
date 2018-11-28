#include<iostream>
#include <fstream> 
#include<string> 
#include<vector>

using namespace std; 

int main()
{
	ifstream in ; 
  	ofstream out; 
	in.open("A-large.in");
	out.open("out.out"); 
	long long T,S; 
	in >>T; 
	string Str; 
	for(int i = 0 ; i <T ; i ++  )
	{ 
		in >> S; 
		in>>Str;
		long long a[S],sum = 0 , c= 0 ; 

		 for(int  k = 0 ; k < Str.length(); k++)
			{
			if(sum < k)
				{
					sum ++ ;
					sum += Str[k]-48; 
					c++ ; 
	 
				}
			else {sum += Str[k]-48; }	
				
			}
		out<<"Case #"<<i+1<<": "<<c<<endl; 
	} 
	
}

#include<iostream>
#include<fstream>

using namespace std ;

int main()
{
   ifstream in("A-small-attempt1.in");
   ofstream out("output.txt") ;
  	int x ;
  	string s ;
  	in>>x ;
  	int m=1 ;
  	getline(in,s);
  	for(int i=0 ; i<x ; i++)
  	{
  	getline(in,s);
  	int count= 0 , sum=0;
  	  for(int i =2 ; i<=(s[0]-'0')+2 ; i++)
  	 {
	  	if((sum+count)<i-1)
	  	count++ ;
	  	sum=sum + (s[i]-'0')  ;
	  }
	  out<<"Case #"<<m++<<":"<<" "<<count-1<<endl ;
  	}    
  
  	
	
	
	
	
	return 0 ;
}
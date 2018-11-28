#include<iostream>
#include<fstream>
#include<memory.h>
#include<string.h>
using namespace std;
	
int main()
{
	
	ifstream fi;
	fi.open("B-large.in",ios::in);
	
	ofstream fo;
	fo.open("B-large.out",ios::out);
	
	
	int test,count;
	char str[2000],temp;
	fi>>test;
	
	fi.getline(str,2000,'\n');
	
	for(int i=0;i<test;i++)
	{
		count=0;
			fi.getline(str,2000,'\n');
			
		
		
	
		
			for(int j=0;j<(strlen(str)-1);j++)
			{
			   if(str[j]!=str[j+1])
			      {
			      	count++;
			      	temp=str[j+1];
			     
			      	for(int k=j;k>=0;k--)
			      	  { 
						 str[k]=temp;
						 
					  }
			       }
			   
			}
		
		if(str[0]!='+')
		 count++;
			  
	    memset(str,0,sizeof(str));
	fo<<"Case #"<<i+1<<":"<<" "<<count<<"\n";
			  
	  
   }
   
   return 0;
   
}

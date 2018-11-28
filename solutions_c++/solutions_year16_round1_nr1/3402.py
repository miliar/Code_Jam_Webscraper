#include<stdio.h>
#include<fstream>
#include<iostream>
#define ll long long


char ptr[2000];


void last(char ch,char str[2000],ll i)
{
	ptr[i]=ch;
	
	
}	
	
void start(char ch, char str[2000],ll i)	
{
	for(ll j=i;j>=1;j--)
	 {ptr[j]=ptr[j-1];
	 	
	 }
	
	ptr[0]=ch;
}	

	
	
	
	
	
	



using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	
	fin.open("input.txt");
	fout.open("output");
	
	ll t,i;
	char str[2000],k[100];
	
	fin>>t;
	fin.getline(k,100);
	 for(ll j=1;j<=t;j++)
	  {fin.getline(str,2000);
	    ptr[0]=str[0];
	    
	    for(i=1;str[i]!='\0';i++)
	     {if(str[i]<ptr[0])
	       last(str[i],str,i);
	        else
	         start(str[i],str,i);
		 }
	  	
	  	ptr[i]='\0';
	  	fout<<"Case #"<<j<<": "<<ptr<<"\n";
	  	
	  	
	  }

 return 0;
}
	


#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<string>
using namespace std;

int main()
{
	
    int t,next=0,max=0,len=0;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	 string word,l;

	  cin>>word;
	 
	  max=word[0];
	  l=word[0];
	  len=word.length();
	  for(int x=1;x<len;x++)
	  {
	  	 next=word[x];
	  	if (next>=max)
	  	{
	  		l=(char)next +l;
	  		max=next;
		  }
		  else
		  {
		  	l=l+(char)next;
		  }
	  }
	  cout<<"Case #"<<i<<": "<<l<<"\n";
	}


    return 0;
}


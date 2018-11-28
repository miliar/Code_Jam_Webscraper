#include<stdio.h>
#include<iostream>
#include<conio.h>
#include <string>
using namespace std;
char rev(char a)
{
	if(a=='+')
	return '-';
	else
	return '+';
}
int check(string a)
{
	for(int q=0;q<a.length();q++)
	{
		if(a[q]=='+')
		return 0;
	
	}
	return 1;
}
int main()
{
	
    int t,count=0;
	cin>>t;
	for(int i=1;i<=t;i++)
	{ count=0;
	 string cake;

	  cin>>cake;
	  //cout<<cake[cake.length()-1];
	  char next='+',now='-';
		  while(1==1)
		  {
		  	if(cake[cake.length()-1]=='+')
			  	{
			  		cake=cake.substr(0,cake.length()-1);
			  		//cout<<cake<<"\n";
			  			continue;
				}
				if(cake.length()==0)
				{cout<<"Case #"<<i<<": "<<0<<"\n";
					break;
				}
				if(check(cake)==1)
				{cout<<"Case #"<<i<<": "<<1<<"\n";
					break;
				}
				count++;
				next=rev(cake[0]);
				now=cake[0];
				for(int j=0;j<10;j++)
				{
					if(cake[j]==now)
					{cake[j]=rev(now);}
					else if(cake[j]==next)
					{break;}
					else
					{}
				}
				
				//cout<<cake<<"\n";
				if(check(cake)==1)
				{count++;cout<<"Case #"<<i<<": "<<count<<"\n";break;}
				
		  }
	}


    return 0;
}


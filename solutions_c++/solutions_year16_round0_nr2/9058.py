#include<iostream>
using namespace std;
#include<stdio.h>
#include<string.h>

char ch[110];
int i,o=1,k,j,h,um,y=1;


void check()
{
	  h=0;
	for(i=k-1;i>=0;i--)
	{
		if(ch[i]=='-')
		{
		    for(j=0;j<=i;j++)
		    {
			if(ch[j]=='-')
			ch[j]='+';
			else
			ch[j]='-';
		    }
		    h++;
   		}
	}
	cout<<"\nCase #"<<y<<": "<<h;
}

int main(void)
{
    cin>>um;
    while(y<=um)
    {
    cin>>ch;
      
	k=strlen(ch);
	check();
	y++;
    }
	return 0;
}




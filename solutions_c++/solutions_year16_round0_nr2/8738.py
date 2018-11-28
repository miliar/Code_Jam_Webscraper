#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
  int t,n,i,r,j,k,f;
   char s[102],ch;
	scanf("%d",&t);
	j=0;
	while(t--)
	{   j++;
	i=0;k=0;f=1;
	    scanf("%s",&s);
	   n=strlen(s);
	   if(s[0]=='-')
	   {f=0;
	       k=1;}
	   for(i=1;i<n;i++)
	   {
	      if(s[i]=='-'  && f==1) 
	      {
	          k+=2;
	      }
	      if(s[i]=='+')
	      f=1;
	      else
	      f=0;
	   }
	    
	    printf("Case #%d: %d\n",j,k);
	  
	}

    return 0;
}


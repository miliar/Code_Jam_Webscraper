#include <stdio.h>
#include <string.h>
using namespace std;
int main(void) {
	int t;
	int flip;
	char s[101],temp;
	scanf("%d",&t);
 
	for(int i=1;i<=t;i++)
	{
	    flip=0;
	    scanf("%s",s);
		int c=strlen(s)-1;
	for(int j=c;j>=0;j--)
	    {
	   if(s[j]=='-')
	   {
	    if(s[0]=='-')
	    {
	        for(int m=j, n=0;m>=n;m--,n++)
	        {
	            temp=s[n];
	            s[n]=s[m];
				s[m]=temp;
	        }
			for(int k=0;k<=j;k++)
	        {
	           if( s[k]=='+')
				   s[k]='-';
			   else
				   s[k]='+';
	        }
	    }
	    else
	    {
	        for(int a=j-1;a>=0;a--)
	        {
	            if(s[a]=='+')
	            {
	             for(int m=a, n=0;m>=n;m--,n++)
	            {
	            temp=s[n];
	            s[n]=s[m];
				s[n]=temp;
	           }
			   for(int k=0;k<=a;k++)
	          {
	           if( s[k]=='+')
				   s[k]='-';
			   else
				   s[k]='+';
	          }
			   break;
 
	          }
	        }
	   }
		 flip++; 
	   }
 
	    }
	    printf("\nCase #%d: %d",i,flip);
	}
	return 0;
}
 
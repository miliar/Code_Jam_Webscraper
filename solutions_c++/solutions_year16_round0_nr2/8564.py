#include <iostream>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	int T,flip;
		cin>>T;
	
	for(int a=1;a<=T;a++)
	{
		
 	char s[1000],temp;
	    cin>>s;
	    flip=0;
	    for(int i=strlen(s)-1;i>=0;i--)
	    {
	        if(s[i]!='+')
	        {
	            if(s[0]=='-')
	            {
	                for(int j=i,k=0;j>=k;j--,k++)
	                {
	                    temp=s[k];
	                    if(s[j]=='+')
	                    s[k]='-';
	                    else
	                    s[k]='+';
	                    
	                    if(temp=='+')
	                    s[j]='-';
	                    else
	                    s[j]='+';
	                }
	                
	            }
	            else
	            {
	               for(int b=i-1;b>=0;b--)
	               {
	                   if(s[b]=='+')
	                   {
	                       for(int j=b,k=0;j>=k;j--,k++)
	                     {
	                    temp=s[k];
	                    if(s[j]=='+')
	                    s[k]='-';
	                    else
	                    s[k]='+';
	                    
	                    if(temp=='+')
	                    s[j]='-';
	                    else
	                    s[j]='+';
	                    } 
	                    break;
	                  }
	               }
	            }
	            flip++;
	        }
	    }
	   cout<<"case #"<<a<<": "<<flip<<endl;
	}

	return 0;
}

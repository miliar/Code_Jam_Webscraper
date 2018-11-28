#include <iostream>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	int t,i,a,fp=0,fm=0,c=0;
	char s[1001];
	cin>>t;
	for(int k=1;k<=t;k++)
	{   fm=0;
	    fp=0;
	    c=0;
	    cin>>s;
	    a=strlen(s);
	    for(i=a-1;i>=0;i--)
	    {
	        if(s[i]=='-' && fp==0)
	         {
	             c++;
	             fp=1;
	             fm=1;
	         }
	        else if(s[i]=='+' && fm==1)
	        {
	            c++;
	            fp=0;
	            fm=0;
	        }
	         
	        
	    }
	    cout<<"Case #"<<k<<": "<<c<<endl;
	    
	}
	
	
	
	
	
	return 0;
}

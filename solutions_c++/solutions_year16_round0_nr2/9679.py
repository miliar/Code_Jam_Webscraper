#include<iostream>
using namespace std;

int main()
{
	int t,i,j,l=0,swap=0;
	string temp,temp1;
	cin>>t;
	string *str = new string[t];
	int *len = new int[t];
	for(i=0;i<t;i++)
    {
    	cin>>str[i];
    	l=str[i].length();
    	len[i]=l;
    }
    
	for(i=0;i<t;i++)
    {	
        swap=0;
		if(str[i][len[i]-1]=='-')
		swap++;
		
		temp=str[i][0];
		
	    for(j=0;j<len[i];j++)
	    {
	    	temp1=str[i][j];
    	  if(temp1!=temp)
    	  swap++;
    	  
    	  temp = temp1;
		  	
    	}
		 cout<<"Case #"<<i+1<<": "<<swap<<"\n";	
    }
    
    return 0;
}
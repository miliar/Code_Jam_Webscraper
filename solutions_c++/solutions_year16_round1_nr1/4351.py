#include<iostream>
using namespace std;

int main()
{
	int t,i,k,j,b,temp;
	cin>>t;
	string *str = new string[t];
	string *str1 = new string[t];
	int *arr = new int[t];
	
	for(i=0;i<t;i++)
	{
		cin>>str[i];
		str1[i]=str[i];
		arr[i]=str[i].length();
	}
	
	for(i=0;i<t;i++)
	{
		b = (int) str[i][0];
		
	for(j=0;j<arr[i];j++)
	{
	    if((int) str[i][j]>=b)	
	    {
	    	b = (int) str[i][j];
	    	
    		for(k=(arr[i]-1);k>=1;k--)
    		{
		    	str1[i][k] = str1[i][k-1];
		    }
		    str1[i][0] = str[i][j];
    	}
    	else
			{
	    	   str1[i][j] = str[i][j];
	        }
	}
	
	cout<<"Case #"<<i+1<<": "<<str1[i]<<"\n";
	}
	
	
	return 0;
}
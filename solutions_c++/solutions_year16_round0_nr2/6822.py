#include <iostream>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	int t,j,i,k,count,c_p,c_n;
	char s[100];
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		cin>>s;
		c_p=0;c_n=0;
		for(i=0;i<strlen(s);i++)
		{
			if(s[i]=='+')
			c_p+=1;
			else c_n+=1;
		}
		if(c_p==strlen(s))
		cout<<"Case #"<<j<<": "<<"0"<<"\n";
		else if(c_n==strlen(s))
		cout<<"Case #"<<j<<": "<<"1"<<"\n";
		else{
			count=0;
			while(c_p!=strlen(s))
			{
				i=1;
				for(;s[0]==s[i];i++);
				if(s[0]=='+')
				{
					count+=1;
					for(k=0;k<i;k++)
					s[k]='-';
					c_p=c_p-(i);
					
				}
				 else if(s[0]=='-')
				{
					count+=1;
					for(k=0;k<i;k++)
					s[k]='+';
					c_p=c_p+i;
				}
			}
			cout<<"Case #"<<j<<": "<<count<<"\n";
		}
	}
	return 0;
}
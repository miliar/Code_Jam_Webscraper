#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int t,count = 0;
	cin>>t;

	for(int i=0;i<t;i++)
	{
		char s[10000];
		cin>>s;
		count=0;		
		for(int j=0;j<strlen(s);j++)
		{
			
			if((s[j]!='+'||s[j+1]=='-')&& s[j+1]!=s[j])
			{
				
				count++;
				if(j==strlen(s)-1 && s[j]=='+') count--;
				s[j]=s[j+1];
					
			}
		}
	cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	//cout<<count<<endl;

	return 0;
}

#include <iostream>
#include <vector>
using namespace std;

int main() {
	unsigned long long int t,y=1;
	cin>>t;
	unsigned long long int count=0;
	char str[102];
	char str2[102];
	while(t--)
	{	
		cin>>str;
		int len;
		str2[0]=str[0];
		int cm=0,cp=0;
		int i=0;
		for(len=0;len<102;len++)
		{	
			if(str[len]=='\0')
				break;
		}
		for(int k=0;k<=len;k++)
		{	
			if(str2[i]!=str[k])
			{
				i++;
				str2[i]=str[k];
			}
		}
		
		for(int j=0; j<=i;j++)
		{		
			if(str2[j]=='-')
			{	cm++;
				
			}
			
		}
		
		char first, last;
		first=str2[0], last=str2[i];
		
		if(first=='-')
		{
			count=1+2*(cm-1);
		}
		else
		{
			count=2*(cm);
		}
		
			cout<<"Case #"<<y<<": "<<count<<endl;
		y++;	
	}
	return 0;
}
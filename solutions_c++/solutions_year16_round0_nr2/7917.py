#include<iostream>
#include<string.h>
using namespace std;

int main()
{
	int t,i,l,j,k,flag=0;
	char s[100];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>s;
		l=strlen(s)-1;
		for(j=l;j>=0;j--)
		{
			if(s[j]=='-')
			{
				for(k=0;k<=j;k++)
				{
					if(s[k]=='+') s[k]='-';
					else s[k]='+';
				}
				flag++;			
			}
		}
		cout<<"Case #"<<i<<": "<<flag<<endl;			
		flag=0;		
	}
	return 0;
}

#include<iostream>
#include<string.h>

using namespace std;

void reverse(char s[],int j)
{
	for(int i=0;i<=j;i++)
	{
		if(s[i]=='-')
			s[i]='+';
		else if(s[i]=='+')
			s[i]='-';
	}
}

int main()
{
	int T;
	cin>>T;

	for(int i=0;i<T;i++)
	{
		char s[100];
		cin>>s;
		
		int len=strlen(s);
		int r=0;
		for(int j=len-1;j>=0;j--)
		{
			if(s[j]=='-')
			{
				reverse(s,j);
				r++;
			}
		}
		cout<<"case #"<<i+1<<": "<<r<<endl;
	}
}

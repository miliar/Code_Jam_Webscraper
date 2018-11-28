#include<iostream>
#include<string.h>
using namespace std;
bool check(char s[1000])
{
	//cout<<s<<endl;
	int i,l=strlen(s);
	for(i=0;i<l;i++)
	{
		if(s[i]=='-')
		return false;
	}
	return true;
	
}
int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		char s[1000];
		cin>>s;
		int j,k,m=0;
		int l=strlen(s);
		//cout<<l;
		for(j=0;j<l;j++)
		{
			bool x=check(s);
			if(x==1)
				break;
			if(x==0)
			{
			if(j+1==l)
			{m++;
				for(k=0;k<l;k++)
				{
					
					if(s[k]=='-')
						s[k]='+';
					else if(s[k]=='+')
						s[k]='-';
				}
				j=-1;
			}
			else if(s[j]=='-' && s[j+1]=='+')
			{m++;
				for(k=0;k<=j;k++)
				{
					if(s[k]=='-')
						s[k]='+';
					else if(s[k]=='+')
						s[k]='-';
				}j=-1;
			}
			//cout<<"likhith "<<j<<endl;

			}
		}
		cout<<"Case #"<<i<<": "<<m<<"\n";
		
		
	}
}

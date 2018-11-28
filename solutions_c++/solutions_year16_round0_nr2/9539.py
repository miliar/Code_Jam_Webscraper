#include<iostream>
# include<cstring>
using namespace std;
char s[101];
int main()
{
	int t,x,i,y,p;
	cin>>t;
	x=t;
	while(t--)
	{
		cin>>s;
		y=0;
		for(i=strlen(s)-1;i>=0;i--)
		{
				pr:
				if(s[i]=='-')
				{
					for(int j=i;j>=0;j--)
					{
							if(s[j]=='+')
								s[j]='-';
							else
								s[j]='+';	
					}					
				    y++;
				}
				p=1;
				for(int k=strlen(s)-1;s[k]>=0;k--)
				{
					if(s[k]=='-')
					{
							i=i-1;
							p=0;
							goto pr;
					}
				}
				if(p==1)
				break;
		}
		cout<<"Case #"<<x-t<<": "<<y<<"\n";
	}
	return 0;
	
}


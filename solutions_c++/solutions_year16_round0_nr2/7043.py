#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int x=0;
	while(x<t)
	{
		x++;
		char s[105];
		cin>>s;
		int i=0;
		int length=strlen(s);
		int count=0,count2=0;
		if(s[i]=='-')
		{
			while(i<length)
			{
				while(s[i]=='-'&&i<length)
					i++;
				while(s[i]=='+'&&i<length)
					i++;
				if(i==length)
					cout<<"Case #"<<x<<": "<<count+1<<endl;
				else
			   	 	count+=2; 
			}
		}
		else
		{
				while(i<length)
				{
					while(s[i]=='+'&&i<length)
						i++;
					if(i==length)
						cout<<"Case #"<<x<<": "<<count<<endl;
					else
					{
				   	 	count+=2; 
						while(s[i]=='-'&&i<length)
							i++;
						if(i==length)
							cout<<"Case #"<<x<<": "<<count<<endl;
					}
				}
			
		}
	}
	return 0;
}
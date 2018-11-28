#include <iostream>
using namespace std;
int main()
{
	int T,cnt,k,i,j,flag,c;
	string str;
	cin>>T;
	c=1;
	while(T--)
	{
		cin>>str;
		cin>>k;
		cnt=0;
		for(i=0;i<str.length()-k+1;i++)
		{
			if(str[i]=='-')
			{
				
				for(j=i;j<i+k;j++)
				{
					if(str[j]=='-')
					{
						str[j]='+';
					}
					else
					{
						str[j]='-';	
					}
				}
				cnt++;

			}
		}
		flag=0;
		for(i=0;i<str.length();i++)
		{
			if(str[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
		{
			cout<<"Case #"<<c<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<c<<": "<<cnt<<endl;
		}
		c++;


	}
	return 0;
}
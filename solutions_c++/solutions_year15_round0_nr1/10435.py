#include<iostream>
using namespace std;
int main()
{
	int t,n,i,id=1,sum,ans;
	char str[1002];
	cin>>t;
	while(t--)
	{
		cin>>n;
		cin>>str;
		sum=str[0]-'0';
		ans=0;
		for(i=1;str[i]!='\0';i++)
		{
			if(str[i]=='0')
			continue;
			if(sum<i)
			{
				ans+=i-sum;
				sum=i+str[i]-'0';
				
			}
			else
			{
				sum+=str[i]-'0';
			}
		}
		cout<<"Case #"<<id<<": "<<ans<<endl;
		id++;
	}	
	return 0;
}
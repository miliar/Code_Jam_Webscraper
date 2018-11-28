#include<iostream>
using namespace std;
int main()
{
	string s;
	int t;
	cin>>t;
	int main=t;
	int arr[100];
	while(t--)
	{
		cin>>s;
		int i=0;
		//cout<<s<<endl;
		//cout<<s[0]<<endl;
		int plus=0,minus=0,count=0,pos,preneg;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='+')
			{
				if(minus!=0)
				{
					count=count+1;
					minus=0;
				}
				plus=plus+1;	
			}
			if(s[i]=='-')
			{
				if(plus!=0)
				{
					count=count+1;
					plus=0;
				}
				minus=minus+1;
			}
		}
		if(minus!=0)
		{
			count=count+1;
		}
		arr[main-t]=count;
		//cout<<count<<endl;
	}
	for(int i=1;i<101;i++)
	{
		cout<<"Case #"<<i<<": "<<arr[i]<<endl;
	}
	return 0;
}

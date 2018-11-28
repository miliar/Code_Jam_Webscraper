#include<bits/stdc++.h>
#define ll long long
#define mod 1000000007
using namespace std;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	
	int test;
	cin>>test;
	for(int t=1;t<=test;t++)
	{
		char str[1005];
		cin>>str;
		int l=strlen(str);
		
		char p=64;
		for(int i=0;i<l;i++)
		{
			p=max(p,str[i]);
		}
	//	cout<<p<<endl;
		
		char front[1005],back[1005];
		int ind1=0;
		int ind2=0;
		int i;
		front[ind1++]=str[0];
		if(str[0]!=p)
		{
			int i;
			for(i=1;i<l;i++)
			{
				if(str[i]==p)
				break;
				if(front[ind1-1]<=str[i])
				front[ind1++]=str[i];
				else
				back[ind2++]=str[i];
			}
			
			for(;i<l;i++)
			{
				if(str[i]==p)
				front[ind1++]=str[i];
				else
				back[ind2++]=str[i];
			}
		}
		else
		{
			for(int i=1;i<l;i++)
			{
				if(str[i]==p)
				front[ind1++]=str[i];
				else
				back[ind2++]=str[i];
			}
		}
		
		cout<<"Case #"<<t<<": ";
		for(int i=ind1-1;i>=0;i--)
		cout<<front[i];
		for(int i=0;i<ind2;i++)
		cout<<back[i];
		cout<<endl;
	}
	return 0;
}

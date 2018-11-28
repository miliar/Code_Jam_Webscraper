#include<stdio.h>
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
  freopen("abc.txt","r",stdin);
 freopen("out.txt","w",stdout);
	int t,sum,count,i,l=0;
	cin>>t;
	while(t--)
	{
		l++;
		sum=0;
		count=0;
		int n;
		cin>>n;
		char str[n];
		cin>>str;
		//for(i=0;i<=n;i++)
		//cin>>arr[i];
		sum=str[0]-'0';
		//cout<<sum<<endl;
		for(i=1;i<=n;i++)
		{
			if(str[i]-'0'==0)
			{
				continue;
			}
			if(str[i]-'0'>0)
			{
				if(sum<i)
				{
				//cout<<"hii"<<endl;
				count=max(count,(i-sum));
				//cout<<count<<endl;
 
 
			}
			sum+=str[i]-'0';
 
			}
		}
		cout<<"Case #"<<l<<": "<<count<<endl;
	}
}

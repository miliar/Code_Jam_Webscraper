#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<cstring>
#include<stack>
using namespace std;

int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int id=1;
	cin>>t;
	while(t--)
	{
		
		string str;
		cin>>str;
		int ans=0,n=str.length(),i=0;
		if(str[0]=='-')
		{
			ans=1;
			while(i<n&&str[i]=='-')
			i++;
		}
		
		while(i<n)
		{
			while(i<n&&str[i]=='+')
			i++;
			int cnt=0;
			while(i<n&&str[i]=='-')
			{
				i++;
				cnt++;
			}
			if(cnt>=1)
			ans+=2;
		}
		
			cout<<"Case #"<<id<<": "<<ans<<"\n";
			id++;
	}
}
 


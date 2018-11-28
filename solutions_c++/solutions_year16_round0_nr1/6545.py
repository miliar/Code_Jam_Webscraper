/**************************************************
 * author:huangjipeng
 * date:2016-3-12
 * filename:temp.cpp
 * ***********************************************/
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
using namespace std;
int cnt[15];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int t;
	cin>>t;
	for(int te=1;te<=t;te++)
	{
		memset(cnt,0,sizeof(cnt));
		long long n;
		cin>>n;
		cout<<"Case #"<<te<<": ";
		if(n==0)
			cout<<"INSOMNIA"<<endl;
		else
		{
			long long i=1,flag=0;
			long long ans,temp;
			while(!flag)
			{
				ans=temp=n*i;
				i++;
				while(temp)
				{
					cnt[temp%10]=1;
					temp/=10;
				}
				flag=true;
				for(int j=0;j<10;j++)
					if(cnt[j]==0)
						flag=false;
			}
			cout<<ans<<endl;
		}
	}
	return 0;
}

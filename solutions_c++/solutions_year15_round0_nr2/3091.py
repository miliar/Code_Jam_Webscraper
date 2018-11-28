#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
	int t;
	cin>>t;
	int curr;
	int p[1001];
	for(curr=1;curr<=t;curr++)
	{
		memset(p,0,sizeof(p));
		int d,i,j;
		int temp;
		int ans=1000000;
		cin>>d;
		for(i=1;i<=d;i++)
		{
			cin>>temp;
			p[temp]++;
		}
		for(i=1;i<=1000;i++)
		{
			temp=i;
			for(j=i+1;j<=1000;j++)
			{
				temp+=((j+i-1)/i-1)*p[j];
			}
		//	cout<<i<<" "<<temp<<endl;
			ans=min(ans,temp);
		}
		printf("Case #%d: %d\n",curr,ans);
	}
	return 0;
}

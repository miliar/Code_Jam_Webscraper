#include<iostream>
#include<cstring>
using namespace std;
int main()
{	freopen("A-large.in","r",stdin);
	freopen("stand3.txt","w",stdout);
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		int smax;
		cin>>smax;
		string shy;
		cin>>shy;
		int len=shy.size();
		//cout<<len;
		int count=shy[0]-'0',ans=0;
		//cout<<count;
		for(int i=1;i<len;i++)
		{
			if(i>count)
			{ans+=i-count;
			count+=i-count;
			count+=shy[i]-'0';}
			else
			{count+=shy[i]-'0';}
			//cout<<count<<"\n";}
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}

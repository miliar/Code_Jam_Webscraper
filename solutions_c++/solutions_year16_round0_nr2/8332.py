#include<bits/stdc++.h>

#define pb(x) push_back(x);
#define gc getchar_unlocked
#define pc(x) putchar_unlocked(x);
#define inf 1<<30
#define ll long long   

using namespace std;

typedef pair<int,int> pii;

int main()
{
	int t,ans,flag;
	string str;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		ans=0;
		cin>>str;
		if(str[0]=='-')
		{
			flag=1;
			ans++;
		}
		else
			flag=0;
		for(int i=1;i<str.size();i++)
		{
			if(str[i]=='+')
			{
				flag=0;
				continue;
			}
			else
			{
				if(flag==0)
				{
					flag=1;
					ans+=2;
				}
			}	
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}

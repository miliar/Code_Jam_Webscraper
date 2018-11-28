#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("s.txt","r",stdin);
	freopen("so.txt","w",stdout);	
	int t,in;
	scanf("%d",&t);
	for(in =1;in<=t;in++)
	{
		int n;
		char s[1005]={'\0'};
		scanf("%d%s",&n,s);
		int i,curr,ans;
		ans = 0;
		curr = 0;
		for(i=0;i<=n;i++)
		{
			if(i>curr)
			{
				ans+=i-curr;
				curr = i;

			}
			curr+=s[i]-'0';
		}
		printf("Case #%d: %d\n",in,ans);
		


	}

}

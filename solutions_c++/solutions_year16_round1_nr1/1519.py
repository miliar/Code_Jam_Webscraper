#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int x=0;
	while(t--)
	{x++;
		char s[10001];
		scanf("%s",s);
		vector<pair<int,char> >v;
		char c,c2;
		int l=1000,r=1000;
		for(int i=0;s[i]!='\0';i++)
		{
			if(i==0)
				{c=s[i];v.push_back(make_pair(l,c));}
			else if(c<=s[i]){ l--;v.push_back(make_pair(l,s[i]));c=s[i];}
			else {r++;v.push_back(make_pair(r,s[i]));}
		}
		sort(v.begin(),v.end());
		printf("Case #%d: ",x);
		for(int i=0;i<(int)v.size();i++)
		{
			printf("%c",v[i].second);
		}
		printf("\n");
	}
	return 0;
}
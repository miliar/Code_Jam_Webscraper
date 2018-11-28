#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
//#include<bits/stdc++.h>

#define pb push_back
#define ll long long int
using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
	ll t,n,i,ans,u;
	char s[1003],ch;
	scanf("%lld",&t);
	for(u=1;u<=t;u++)
	{
		ans=0;
		scanf("%s",s);
		ch=s[0];
		n=strlen(s);
		for(i=1;i<n;i++)
		{
			if(s[i]!=ch)
			{
				ans++;
				if(ch=='-')
					ch='+';
				else
					ch='-';
			}
		}
		if(ch=='-')
			ans++;
		printf("Case #%lld: %lld\n",u,ans);
	}

	return 0;
}

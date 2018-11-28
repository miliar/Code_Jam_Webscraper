#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
//#include<bits/stdc++.h>

#define pb push_back
#define ll long long int
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
  	freopen("output.txt","w",stdout);
	ll t,n,i,ans,u,x,h,c,v,c1;
	char k='A',k1='A';
	scanf("%lld",&t);
	for(u=1;u<=t;u++)
	{
		printf("Case #%lld: ",u);
		c1=0;
		scanf("%lld",&n);
		map <char,long long int> mp;
		map <char,long long int>::iterator it;
		for(i=0;i<n;i++)
		{
			scanf("%lld",&x);
			mp['A'+i]=x;
			c1+=x;
		}
		for(;c1!=0;)
		{
			h=0;
			for(it=mp.begin(),i=0;i<n;it++,i++)
			{
				h=max(h,mp['A'+i]);
			}

			c=0;
			for(it=mp.begin(),i=0;i<n;it++,i++)
			{
				if(mp['A'+i]==h)
				{
					c++;
				}
			}
			//printf("h=%lld c=%lld\n",h,c);
			if(c%2==1)
			{
				for(it=mp.begin(),i=0;i<n;it++,i++)
				{
					if(mp['A'+i]==h)
					{
						k='A'+i;
						mp[k]--;
						c1--;
						break;
					}
				}
			}
			else
			{
				v=2;
				for(it=mp.begin(),i=0;i<n;it++,i++)
				{
					if(v==0)
						break;
					if(mp['A'+i]==h&&v==1)
					{
						k1='A'+i;
						mp[k1]--;
						v--;
						c1--;
					}
					if(mp['A'+i]==h&&v==2)
					{
						k='A'+i;
						mp[k]--;
						v--;
						c1--;
					}
				}
			}
			if(c%2==1)
				printf("%c ",k);
			else
				printf("%c%c ",k,k1);
		}
		printf("\n");
	}
	return 0;
}


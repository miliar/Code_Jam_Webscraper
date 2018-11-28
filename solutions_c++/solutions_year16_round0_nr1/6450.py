#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
#include<set>
//#include<bits/stdc++.h>

#define pb push_back
#define ll long long int
using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
	ll t,n,i,ans,temp,b,u,ori;
	set<long long int> s;
	set<long long int>::iterator it;
	scanf("%lld",&t);
	for(u=1;u<=t;u++)
	{
		scanf("%lld",&n);
		ori=n;
		if(n==0)
			printf("Case #%lld: INSOMNIA\n",u);
		else
		{
			for(i=0;i<10;i++)
				s.insert(i);
			for(i=1;;)
			{
				temp=n;
				//printf("n=%lld\n",n);
				while(temp>0)
				{
					b=temp%10;
					it=s.find(b);
					if(it!=s.end())
						s.erase(it);
					temp/=10;
				}
				if(s.size()==0)
				{
					printf("Case #%lld: %lld\n",u,n);
					break;
				}
				i++;
				n=ori*i;
			}
		}
	}

	return 0;
}

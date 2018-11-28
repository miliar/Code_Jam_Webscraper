//Author: sagarkaniche
#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define si(x) scanf("%d",&x)
#define sdb(x) scanf("%lf",&x)
#define sll(x) scanf("%lld",&x)
#define pb push_back
#define res 1000000007
typedef pair<int,int> pp;


int main()
{
	ll maxx=0,i,j;
	for(i=0;i<=9;i++) maxx|=(1<<i);
	int t,cnt=1;
	si(t);
	while(t--)
	{
		ll n;
		sll(n);
		ll ans=0,temp;
		for(j=1;j<=100;j++)
		{
			temp = n*j;
			while(temp)
			{
				int ind=temp%10;
				ans|=(1<<ind);
				temp/=10;
			}
			if(ans==maxx)
			{ 
				printf("Case #%d: %lld\n",cnt++, n*j);
				break;
			}
		}
		if(ans!=maxx){printf("Case #%d: INSOMNIA\n",cnt++);}
	}

	
	return 0;
}
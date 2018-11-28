#include<bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define si(i) scanf("%d",&t)
#define sll(i) scanf("%lld",&i)
#define fs first
#define sc second
#define FOR(i,j,k) for(int i=0;i<k;i++)
#define REP(i,k) for(int i=0;i<k;i++)
#define FORR(i,j,k) for(int i=n;i>=k;i--)
#define MOD 1000000007
using namespace std;
int main()
{
	//Let's start
	int t;
	ll n;
	si(t);
	//map<ll,bool>m;
	int Case =1;
	while(t--)
	{
		sll(n);
		bool hash[10]={false};
		int count =0;
		int i=1;
		if(n == 0)
		{
			printf("Case #%d: INSOMNIA\n",Case++);
			continue;
		}
		ll tmp;
		while(1)
		{
			tmp = (i*n);
			while(tmp > 0)
			{
				if(hash[tmp%10] == false)
				{
					hash[tmp%10] = true;
					count++;
				}
				tmp/=10;
			}
			if(count > 9)
			{
				break;
			}
			i++;
		}
		printf("Case #%d: %lld\n",Case++,i*n);
	}
	return 0;
}

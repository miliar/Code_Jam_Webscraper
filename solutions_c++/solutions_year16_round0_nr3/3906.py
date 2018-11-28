#include<bits/stdc++.h>
#define ll long long 
#define pb push_back
#define mp make_pair
#define si(i) scanf("%d",&i)
#define fs first
#define sc second
#define FOR(i,j,k) for(int i=j;i<k;i++)
#define REP(i,k) for(int i=0;i<k;i++)
#define FORR(i,j,k) for(int i=n;i>=k;i--)
#define MOD 1000000007
using namespace std;
ll arr[10];
ll baseConvo(ll a,int b)
{
	ll res =0,multiplier=1;
	while(a>0)
	{
		res += (a%b)*multiplier;
		multiplier*=10;
		a/=b;
	}
	return res;
}
ll tobase(ll a,int b)
{
	
	ll ans=0,mul=1;
	while(a>0)
	{
		ans += (a%10)*mul;
		a/=10;
		mul *= b;
	}
	//cout << a << " " << b << " " << ans << endl;
	return ans;

}
bool checkPrime(ll ans,int base)
{
	
	for(ll i=2;i*i<=ans;i++)
	{
		if(ans%i == 0)
		{
			arr[base] = i;
			return true;
		}
		//cout << "1" << endl;
	}
	return false;
}
int main()
{
	//Let's start
	int n,J,t;
	si(t);
	int Case=1;
	//cout << t << endl;
	while(t--)
	{

	//cout << t << endl;
		int count=0;
		si(n);si(J);
		//cout << n << " " << J << endl;
		printf("Case #%d:\n",Case++);
		ll res;
		ll l = (1<<14);
		ll ans = (1<<15) + 1;
		for(int i=0;i<l;i+=2)
		{
			int flag =0;
			ll res = baseConvo(ans + i,2);
			FOR(j,2,11)
			{

				ll ans1 = tobase(res,j);
				if(checkPrime(ans1,j-2)==false)
				{
					flag =1;
					break;
				}
			}
			if(flag == 0 )
			{
				printf("%lld ",res);
				REP(k,9)
				{
					printf("%lld ",arr[k]);
				}
				printf("\n");
				count++;
				if(count == J)
					break;
			}
		}
		//printf("2\n");
	}
	return 0;
}
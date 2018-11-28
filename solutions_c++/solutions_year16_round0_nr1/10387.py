#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll res[1000001];

void preprocess()
{
	ll cache[10];
	for(ll i=1; i<=1000000; i++)
	{
		memset(cache, 0, sizeof(cache));
		ll n = i, temp, flag = 1, count = 1, ans = 0, fix = n;
		while(flag)
		{
			temp = n;
			while(temp)
			{
				if(!cache[temp%10]) cache[temp%10] = 1, ans++;
				if(ans==10)
				{
					flag = 0;
					res[i] = n;
					break;
				}
				temp /= 10;
			}
			count++;
			n = fix*count;
		}
	}
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	preprocess();
	ll t, n;
	scanf("%lld", &t);
	for(int i=1; i<=t; i++)
	{
		scanf("%lld", &n);
		cout<<"Case #"<<i<<": ";
		if(n==0) cout<<"INSOMNIA"<<endl;
		else cout<<res[n]<<endl;
	}
	return 0;
}

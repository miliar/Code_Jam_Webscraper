#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//#define mod 1000000007
#define ll long long int
#define maxn 1000005
#define seive_max 10000

using namespace std;

bool check(ll ar[], ll per[], ll n)
{
	bool ans = true;

	ll i = 0;
	

	while(i<n-1 && ar[per[i]]<ar[per[i+1]])
		i++;

	if(i==n-1)
		return true;

	while(i<n-1 && ar[per[i]]>ar[per[i+1]])
		i++;

	if(i==n-1)
		return true;

	return false;
}

int main()
{
	ll t, b;
	cin>>t;
	for(ll c=1; c<=t; c++)
	{
		ll n, x, i, j;
		
		cin>>n;
		ll ar[n];

		for(i=0; i<n; i++)
			cin>>ar[i];

		ll per[n];
		for(i=0; i<n; i++)
			per[i] = i;
		ll count = -1;
		do
		{
			bool ans;
			i = 0;
			while(i<n-1 && ar[per[i]]<ar[per[i+1]])
				i++;

			if(i==n-1)
				ans = true;

			else
			{
				while(i<n-1 && ar[per[i]]>ar[per[i+1]])
					i++;

				if(i==n-1)
					ans = true;
				else
					ans =  false;
			}
			//bans = check(per, ar, n);
			if(ans)
			{
				int temp = 0;
				ll temp_ar[n];
				for(i=0; i<n; i++)
					temp_ar[i] = i;

				for(i=0; i<n; i++)
				{
					if(temp_ar[i]!=per[i])
					{
						for(ll j=i+1; j<n; j++)
						{
							if(temp_ar[j]==per[i])
							{
								temp += j-i;
								for(ll k=j; k>i; k--)
									temp_ar[k] = temp_ar[k-1];
								break;
							}
						}
					}
				}

				if(count==-1 || temp<count)
				{
					/*for(i=0; i<n; i++)
						cout<<per[i]<<" ";
					cout<<endl;*/
					count = temp;

					//cout<<temp<<count<<endl;
				}
			}
		}while(next_permutation(per, per+n));

		cout<<"Case #"<<c<<": "<<count<<endl;;

	}
	return 0;
}
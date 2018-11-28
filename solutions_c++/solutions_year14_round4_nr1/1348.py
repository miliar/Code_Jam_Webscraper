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

void print_case(ll i)
{
	cout<<"Case #"<<i<<": ";
}

ll ar[100000];

int main()
{
	ll t, b;
	cin>>t;
	for(ll c=1; c<=t; c++)
	{
		ll n, x, i, j;
		cin>>n>>x;
		for(i=0; i<n; i++)
			cin>>a[i];

		sort(a, a+n);

		ll count = 0;
		i = 0, j=n-1;
		ll ctr = 0;
		while(i<j)
		{
			if(a[i]+a[j]<=x)
			{
				count++;
				i++;
				j--;
			}
			else
			{
				count++;
				j--;

				if(i==j)
				{
					count++;
					ctr = 1;
				}
			}
		}

		print_case(c);
		if(ctr==1 || i>j)
			cout<<count<<endl;
		else
			cout<<count+1<<endl;

	}
	return 0;
}
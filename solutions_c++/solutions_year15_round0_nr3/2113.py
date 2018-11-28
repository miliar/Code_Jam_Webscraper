#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
#include <math.h>

#define max_nodes_size 100005
#define max_log_size 17
#define ll int
#define mod 1000000007

#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define INF 0x3f3f3f3f
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) typeof(v) r = (v)
#endif
	
using namespace std;

char word[10005];
ll pre[10005];

char find_next(ll last, ll cur)
{
	if(last=='i' || last=='s')
	{

	}
}

ll matrix[5][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};

ll find_index(char ch)
{
	if(ch=='i')
		return 2;

	if(ch=='j')
		return 3;

	return 4;
}

int main()
{
	ll t;
	cin>>t;
	for(ll counter=1; counter<=t; counter++)
	{
		ll l, x;
		cin>>l>>x;
		string w;
		cin>>w;

		for(ll i=0; i<x; i++)
			for(ll j=0; j<l; j++)
				word[i*l+j] = w[j];

		ll i=0, j=0, k=0;
		pre[0] = find_index(word[0]);

		if(pre[0]==2)
			i = 1;

		for(ll m=1; m<l*x; m++)
		{
			ll flag = 0;
			if(pre[m-1]<0)
				flag = 1;

			ll temp = abs(pre[m-1]);
			ll temp2 = find_index(word[m]);
			ll ans = matrix[temp][temp2];
			if(flag)
				ans = -ans;

			pre[m] = ans;
			if(i==1 && pre[m]==4)
				j = 1;

			if(i==0 && pre[m]==2)
				i = 1;
		}

		if(j==1 && pre[l*x-1]==-1)
			k = 1;
		
		cout<<"Case #"<<counter<<": ";
		if(i+j+k==3)
			cout<<"YES\n";
		else
			cout<<"NO\n";
	}
	return 0;
}
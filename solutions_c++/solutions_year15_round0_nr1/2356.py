#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;
#define clear(a) memset((a),0,sizeof(a))
#define pb push_back
#define SIZE(v) v.size()
#define ull unsigned long long int
#define lli long long int
#define li long int
#define ii int
#define mod 1000000007
/* Created by : Rahul Johari
				Thapar University */
				
int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	lli t,i,max,sum,c,cse;
	string s;
	
	scanf("%lld",&t);
	for ( cse=1;cse<=t;cse++ )
	{
		sum = c = 0;
		scanf("%lld",&max);
		cin >> s;
		lli a[max+1];
		//cout << s << endl;
		for ( i=0;i<max+1;i++ )
		{
			a[i] = s[i]-'0';
			if ( i>sum )
			{
				c += 1;
				sum += 1;
			}
			sum += a[i];
		}
		printf("Case #%lld: %lld\n",cse,c);
	}
    return 0;
}

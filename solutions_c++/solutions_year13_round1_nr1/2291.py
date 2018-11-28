#include<iostream>
#include<stack>
#include<map>
#include<utility>
#include<stdlib.h>
#include<math.h>
#include<stdio.h>
#include<map>
#include<fstream>
#include<algorithm>
#include<bitset>
#include<vector>
#include<cstring>
using namespace std;
#define mp make_pair
#define f first
#define pb push_back
#define s second
#define ull unsigned long long
#define ll long long
#define ui unsigned int
#define MOD 1000000007

int gcd(int a, int b)
{
    while( 1 )
    {
	a = a % b;
	if( a == 0 )
	    return b;
	b = b % a;

	if( b == 0 )
	    return a;
    }
}

int main()
{
    int T;
    cin>>T;
    for(int test=1;test<=T;test++)
    {
	ll t,r;
	cin>>r>>t;
	r++;
	ll ans =0,tt=0;
	while(tt<=t)
	{
	    tt+=(r*r-(r-1)*(r-1));
	    ans++;
	    r+=2;
	}
	cout<<"Case #"<<test<<": "<<(ans-1)<<endl;
    }
    return 0;
}

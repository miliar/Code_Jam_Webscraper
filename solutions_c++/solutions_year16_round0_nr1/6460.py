#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>

#include <math.h>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;


#define Max 10000000  

int num = 0;
int ft[20];

int check( int n )
{
	while( n > 0 ){
		if( ft[n%10] == 0 ) ++num;
		ft[n%10]=1;
		n/=10;
		if( num >= 10 )
			return 1;
	}
	return 0;
}

int solve( int n )
{
	int t = n;
	for( int i = 1; ; ++i )
	{
		t=n*i;
		if( check( t ) )
			return t;
	}
	return 0;
}

int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		num = 0;
		clr( ft );
		int  n;
		cin>>n;
		if( n == 0 )
			printf("Case #%d: INSOMNIA\n", c+1);
		else
			printf("Case #%d: %d\n",c+1,solve(n));
	}
}

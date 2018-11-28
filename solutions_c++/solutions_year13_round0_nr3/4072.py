#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <string>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cstdio>
using namespace std;
#define ll long long
#define N 11000000

ll v[N];
// ll par[N];
ll n;
char s[32];

bool ispal(ll x)
{
	int i = 0;
	// cout << x << endl;
	while(x)
	{
		s[i ++] = x%10 + '0';
		x /= 10;
	}
	/*
	for(int j = 0; j < i; j ++)
		cout << s[j];
	cout << " " << i << endl << endl;
	//*/
	
	i --;
	int j = 0;
	while(j <= i)
	{
		if(s[i] != s[j])
			return false;
		i --;
		j ++;
	}
	return true;
}

int main()
{
	ll x = 1;
	n = 0;
	while(x*x <= 100000000000000ll)
	{
		if(ispal(x) && ispal(x*x))
		{
			// cout << x << " " << x*x << endl;
			v[n] = x*x;
			// par[n] = x;
			n ++;
		}
		x ++;
	}
	
	int test, res;
	ll a, b;
	
	cin >> test;
	for(int cas = 1; cas <= test; cas ++)
	{
		cin >> a >> b;
		res = 0;
		for(int i = 0; i < n; i ++)
			if(a <= v[i] && v[i] <= b)
				res ++;
		printf("Case #%d: %d\n", cas, res);
	}
	
	return 0;
}


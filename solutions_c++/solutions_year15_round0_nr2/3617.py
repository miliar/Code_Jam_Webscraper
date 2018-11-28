#include <bits/stdc++.h>

using namespace std;

int v[1001];
int n;

bool step( int s , int y )
{
	int q = 0;
	for (int i = 0; i < n; ++i)
	{	q+=(v[i]/y);
		if( v[i]%y==0 ) q--;
	
	}
	if( q <= s ) return true;
	return false;
}

bool f( int x )
{
	for (int i = 0; i < x; ++i)
		if( step( i,x-i )==true ) return true;
	return false;
}

int main()
{
	#ifndef ONLINE_JUDGE
   	freopen("input.txt", "rt", stdin);
   	freopen("output.txt", "wt", stdout);
	#endif
	int T;
	cin >> T;
   	for (int cas = 0; cas < T; ++cas)
   	{
   	cin >> n;
   	for (int i = 0; i < n; ++i)
   		cin >> v[i];

   	int l = 0,r = 1001;

   	while( r - l > 1 )
   	{
   		int mid = r+l;
   		mid/=2;
   		if( f(mid)==true ) r = mid;
   		else l = mid;
   	}

   	cout <<"Case #"<<cas+1<<": "<< r << endl;
   	}
}
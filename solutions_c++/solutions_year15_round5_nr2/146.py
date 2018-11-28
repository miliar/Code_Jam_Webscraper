#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cassert>
using namespace std; 
int n,k; 
int s[100000],mins[100000],maxs[100000],temp[100000]; 

int main()
{
	int it=0;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T; 
	scanf( "%d" , &T ); 
	while ( T-- ) 
	{
		++it;
	scanf( "%d %d" , &n,&k ); 
	for ( int i=1; i<=n-k+1; i++ ) scanf( "%d" , &s[i] ); 
	for ( int i=0; i<=n; i++ ) { mins[i] = 0; maxs[i] = 0; temp[i] = 0; } 
	for ( int i=1; i<n-k+1; i++ ) 
	{
		temp[i%k] += s[i+1]-s[i]; 
		mins[i%k] = min( mins[i%k] , temp[i%k] );  
		maxs[i%k] = max( maxs[i%k] , temp[i%k] ); 
	}
	int ans = 0; 
	for ( int i=0; i<k; i++ ) ans = max( ans , maxs[i]-mins[i] ); 
	for ( int d=ans; ; d++ ) 
	{
			int p1 = 0,p2 = 0; 
			for ( int j=0; j<k; j++ ) p1 += -mins[j]; 
			for ( int j=0; j<k; j++ ) p2 += d-maxs[j];
			int temp = p1/k; p1 -= k*temp; p2 -= k*temp;
			p1+=k;p2+=k;
			temp = p1/k; p1 -= k*temp; p2 -= k*temp; 
			s[1]%=k;s[1]+=k;s[1]%=k;
			if ( (p1 <= s[1] && s[1] <= p2) || (p1 <= s[1]+k && s[1]+k <= p2) ) 
			{ printf( "Case #%d: %d\n" ,it, d ); break; }
			
	}
	}
}

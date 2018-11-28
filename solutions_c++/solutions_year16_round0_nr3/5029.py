#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
int J;
ll toNum( string num , ll base )
{
	ll n = 0;
	for( int i = 0 , len = num.size() ; i < len ; i++ )
	{
		n = n * base + (num[i] - '0');
		//cerr << n << endl;
	}
	return n;
}
int findDivisor( string num , ll base )
{
	ll n = 0;
	for( int i = 0 , len = num.size() ; i < len ; i++ )
	{
		n = n * base + (num[i] - '0');
		//cerr << n << endl;
	}
	for( ll i = 2 ; i * i <= n ; i++ )
		if( n % i == 0 ) 
		{
			return i;
		}
	return 0;
}
void recur( int n , string num )
{
	if( J == 0 ) return;
	
	if( n == 0 )
	{
		num.push_back('1');
		int a[12];
		bool ok = true;
		for( int base = 2 ; base <= 10 ; base++ )
		{
			a[base] = findDivisor( num , base );
			if( a[base] == 0 )
			{
				ok = false;
				break;
			}
		}
		if(ok)
		{
			cout << num << " ";
			for( int base = 2 ; base <= 10 ; base++ )
				printf( "%d " , a[base] );
			printf("\n");
			J--;
		}
	}
	else
	{
		n--;
		num.push_back('0');
		recur( n , num );
		num[num.size() - 1] = '1';
		recur( n , num ); 
	}
}
int main()
{
	//freopen("a.inp","r",stdin);
	//freopen("a.out","w",stdout);
	int T , N;
	
	scanf("%d",&T);
	scanf("%d%d",&N,&J);
	
	printf("Case #1:\n");
	recur( N - 2 , "1" );	
	return 0;
}

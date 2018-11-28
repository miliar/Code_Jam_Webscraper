#include<iostream>
#include<cstdio>
#include<bitset>
using namespace std;

int t, n, j, jest[20], ile;
bitset<40> foo;
bool blad;
bool dziel( int pod, int d )
{
	int sum = 0;
	int pot = 1;
	for( int a = 0; a < n; a++ )
	{
		if( foo[a] )sum += pot;
		sum %= d;
		pot *= pod;
		pot %= d;
	}
	if( sum == 0 )return 1;
	return 0;
}	
int main()
{
//	freopen( "B-large.in", "r", stdin );
	freopen( "dane.txt", "w", stdout );
	ios_base::sync_with_stdio( 0 );
	cin>>t;
	cin>>n>>j;
	cout<<"Case #1:"<<endl;
	for( int a = 0; a <= 1000000; a += 2 )
	{
		blad = 0;
		for( int b = 2; b <= 10; b++ )jest[b] = 0;
		foo = a;
		foo[0] = 1;
		foo[n-1] = 1;
		for( int b = 2; b <= 10; b++ )
		{
			for( int c = 2; c <= 11; c++ )
			{
				if( dziel( b, c ) )
				{
					jest[b] = c;
					break;
				}
			}
			if( jest[b] == 0 )
			{
				blad = 1;
				break;
			}
		}
		if( !blad )
		{
			for( int b = n-1;  b >= 0; b-- )cout<<foo[b];
			cout<<" ";
			for( int b = 2; b <= 10; b++ )cout<<jest[b]<<" ";
			cout<<endl;
			++ile;
			if( ile == j )break;
		}
	}
//	cout<<ile<<endl;
	return 0;
}

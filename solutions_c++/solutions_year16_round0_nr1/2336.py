#include<iostream>
#include<cstdio>

using namespace std;

int t, x, v;
bool jest[1010], blad;

void cnt( int x )
{
	while( x )
	{
		jest[ x%10 ] = 1;
		x /= 10;
	}
}
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "dane.txt", "w", stdout );
	cin>>t;
	for( int a = 1; a <= t; a++ )
	{
		for( int b = 0; b < 10; b++ )jest[b] = 0;
		blad = 0;
		cin>>x;
		v = x;
		if( x == 0 )cout<<"Case #"<<a<<": INSOMNIA"<<endl;
		else while( 1 )
		{
			cnt( v );
			blad = 0;
			for( int b = 0; b < 10; b++ )if( !jest[b] )blad = 1;
			if( !blad )
			{
				cout<<"Case #"<<a<<": "<<v<<endl;
				break;
			}
			v += x;
		}
	}
	return 0;
}

#include<cstdio>

long long r,p;

bool ck( long long a , long long b )
{
	int i = 0;
	while( a > 0LL ) a /= 10LL, i ++;
	while( b > 0LL ) b /= 10LL, i ++;
	return ( i <= 19 );
}

long long bs( long long f , long long l )
{
	if( f >= l ) return f;
	long long m = ( f + l +1 ) / 2;
	if( !ck( 2LL*m , r ) or !ck( 2LL*m - 1 , m ) ) return bs( f , m - 1LL );
	long long v = 2LL*m*r + ( 2LL*m - 1 )*( m );
	if( v > p ) return bs( f , m - 1LL );
	else return bs( m , l );
}

void len()
{
	scanf("%lld%lld",&r,&p);
	long long z = bs( 1 , 1000000000LL );
	printf("%lld\n",z);
}


int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int o;
	scanf("%d",&o);
	for(int c=1;c<=o;c++)
	{
		printf("Case #%d: ",c);
		len();
	}
}

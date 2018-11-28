#include<cstdio>
#include<cstring>
int P[1001];

inline void clearP()
{
	memset( P , 0 , sizeof(P));
}

inline int next(const int p)
{	
	for ( int k( p-1) ; k > 0 ; --k )
		if(P[k] > 0)
			return k;

	return 1;
}
inline int isbetter( const int k )
{
	if( k == 2 )
		return 2;
	if( k == 1)
		return 1;
	if( k == 3)
		return 3;
	
	int nb = P[k];
	int t(k);
	for( int j(1) ; j <= k/2 ; ++j)
	{
		P[j] += nb;
		P[k - j] += nb;
		
		int tmp = isbetter( next(k));
		P[j] -= nb;
		P[k - j] -= nb;

		if(tmp < t)
			t = tmp;
	}

	if(t + nb <= k)
		return t + nb;
	else
		return k;
}

int main()
{

	int T;
	std::scanf("%d", &T );
	
	for (int t(1) ; t <= T ; ++t)
	{
		//init
		int D;
		clearP();
		std::scanf("%d", &D);
		//std::printf("%d\n", D);
		int tmp, st(0);

		for( int i(0) ; i < D ; ++i)
		{
			std::scanf("%d" , &tmp );
			//std::printf("%d " , tmp );
			P[ tmp ] ++;
			if(tmp > st)
				st=tmp;
		}
			//std::printf("\n");
			int out = isbetter( st );
			std::printf("Case #%d: %d\n",t , out);
	
		// processing
	}
	return 0;
}

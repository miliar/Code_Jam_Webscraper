#include<iostream>

inline int charToInt( const char a)
{
	return int(a) - 48;
}

inline void affich(const int a , const int b)
{
	std::cout << "Case #" << a <<": " << b <<'\n';
}
int main()
{
	std::ios::sync_with_stdio(false);
	int T, cardS;
	char S[1010];

	std::cin >> T;
	

	for( int i(1) ; i <= T ; ++i)
	{
		std::cin >> cardS >> S;
		int Tot(0), out(0);

		for( int j(0) ; j <= cardS ; ++j )
		{
			int tmp = charToInt( S[j] );

			if(Tot < j )
			{
				out += j - Tot;
				Tot += j - Tot;
				Tot += tmp;
			}
			else
				Tot += tmp;
		}
		affich( i, out );
	}


	return 0;
}

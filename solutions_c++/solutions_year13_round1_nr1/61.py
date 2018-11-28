#include <cstdio>
#include <iostream>
#include <gmpxx.h>
typedef mpz_class mpz;
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		mpz R,A;
		std::cin >> R >> A;
		mpz n=0;
		mpz A1=2*R+1;
		if(A1<=A)
		{
			mpz a=2*R-1;
			mpz d=a*a+8*A;
			mpz s=sqrt(d);
			n=(1-2*R+s)/4;
		}
		std::cout << "Case #" << t << ": " << n << std::endl;
	}
}

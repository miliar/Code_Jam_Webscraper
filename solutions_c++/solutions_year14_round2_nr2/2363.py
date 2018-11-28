#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <stdlib.h>

#define INF 1000000015

using namespace std;



int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, t, i, j, A, B, K, s;
	char buff[9];
	bool checker;
	scanf("%d", &T);
	for(t=0; t<T; ++t)
	{
		
		scanf("%d %d %d", &A, &B, &K);
		s=0;
		for (i=0; i<A;++i)
			for(j=0; j<B; ++j)
			{
				if ((i&j)<K)
					++s;
			}
		printf("Case #%d: ",t+1);
		printf("%d\n", s);

	}	

	return 0;
}
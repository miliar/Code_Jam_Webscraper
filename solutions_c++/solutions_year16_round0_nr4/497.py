#include <stdio.h>
#include <iostream>
#include <algorithm>

// #include <random>
// #include <math.h>
// 


int main()
{
// 	printf("100\n");
// 	std::uniform_int_distribution<int> dist(1, 100);
// 	for(int i=0; i<100; ++i)
// 	{
// 		int k=dist(std::random_device());
// 		int c=dist(std::random_device());
// 		double dk=k, dc=c;
// 		if(pow(dk, dc)>1000000000000000000.0)
// 		{
// 			--i; 
// 			continue;
// 		}
// 		printf("%d %d %d\n", k, c, k);
// 	}
// 	return 0;
// 

	int cases;
	std::cin >> cases;

	int64_t tile_selector[100];
	int64_t m[100];

	for(int case_counter=0; case_counter<cases; ++case_counter)
	{
		int64_t k, c, s;
		std::cin >> k >> c >> s;
		if(s<(k+c-1)/c)
		{
			printf("Case #%d: IMPOSSIBLE\n", case_counter+1);
			continue;
		}

		for(int64_t i=0; i<c; ++i)
		{
			tile_selector[i]=std::min(i,k-1);
		}
		m[0]=1;
		for(int64_t i=1; i<c; ++i)
		{
			m[i]=m[i-1]*k;
		}
		printf("Case #%d:", case_counter+1);
		for(;;)
		{
			int64_t tile_to_check=0;
			for(int64_t i=0; i<c; ++i)
			{
				tile_to_check+=tile_selector[i]*m[i];
			}
			printf(" %lld", tile_to_check+1);

			if(tile_selector[c-1]==k-1)
				break;
			for(int64_t i=0; i<c; ++i)
			{
				tile_selector[i]=std::min(tile_selector[i]+c, k-1);
			}
		}
		printf("\n");
	}
	return 0;
}
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <map>
#include <cmath>

using namespace std;

int main()
{
	int T, K, C, S;

	scanf("%d", &T);

	for(int t = 1; t <= T; ++t)
	{
		scanf("%d %d %d", &K, &C, &S);

 		long long kc = 1;
 		for(int i = 0; i < C; ++i)
 			kc *= K;

 		printf("Case #%d:", t);

 		//long long ind = kc/2 - S/2;
 		//if(ind == 0) ind = 1;
 		
 		for(int i = 0; i < S; ++i)
 			printf(" %d", i+1);
 		printf("\n");
	}


	return 0;
}
#include <iostream>
#include <cstdio>
#include <bitset>

using namespace std;

int main()
{
	int T, A, B, K;
	int i, a, b, count;
	std::bitset< 32 > num1, num2, num3;
	unsigned long ul;


	scanf("%d",&T);
	for( i = 1; i <= T; i ++ ) {
		scanf("%d %d %d", &A, &B, &K);
		
		count = 0;
		for( a = 0; a < A; a ++ ) {
			num1 = a;
			for( b = 0; b < B; b ++ ) {
				num2 = b; 
				num3 = num1 & num2;
				ul = num3.to_ulong();	
				if( ul < K ) {
					count ++;
				}
			}
		}
		printf("Case #%d: %d\n", i, count);
	}

	return 0;
}

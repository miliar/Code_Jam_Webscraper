#include<stdio.h>
#include<string.h>
#include<algorithm>
#define INF 999999999
using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output_B_small.txt", "w", stdout);
	long long int TC, T, A, B, K, i, j;
	long long int count=0;
	scanf("%lld", &TC);
	for (T = 1; T <= TC; T++){
		printf("Case #%lld: ", T);
		scanf("%lld%lld%lld", &A, &B, &K);
		for (i = 0; i < A; i++){
              for (j = 0; j < B; j++){
                  if((i&j)<K){
                             count++;
                             //printf("%lld%lld\n", i,j);
                             }
                             }
                             }
  printf("%lld\n", count);
  count=0;
	}
return 0;
}

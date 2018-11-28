#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<vector>
#include<cstring>
#include<math.h>
using namespace std;

unsigned long long r, t;
unsigned long long num;

void Solve()
{
	unsigned long long delta = 4 * r * r - 4 * r + 1 + 8* t;	
	num = (1 - 2 * r + (unsigned long long)sqrt((double)delta)) / 4;
}

int main()
{
	int T;
	cin>>T;
	for (int i = 1; i <= T; i++) {
		scanf("%lld %lld", &r, &t);
		Solve();
		printf("Case #%d: %lld\n", i,  num);
	}
	return 0;
}

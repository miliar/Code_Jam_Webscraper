#include <stdio.h>
#include <string.h>
#include <algorithm>


using namespace std;

typedef long long int llint;

void doet()
{
	llint a,b,da,db;
	int n;
	llint p;
	scanf("%d%lld", &n, &p);
	llint u = 1<<n;
	if (p == u) {printf("%lld %lld\n", u-1, u-1); return;}
	if (p == 1) {printf("0 0\n"); return;}

	/*if (p <= u/2) {
		printf("0 ");
	} else {//*/
	a = u-2;
	b = u-1;
	da = u/2;
	db = 2;
	while (p < b) {
		a -= da; da /= 2;
		b -= db; db *= 2;
	}
	printf("%lld ", a);
	//}

	a = u-2;
	b = u/2;
	da = 2;
	while (p < b) {
		a -= da; da *= 2;
		b /= 2;
	}
	printf("%lld\n", a);
}


int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		doet();
	}
	return 0;
}


#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define LL long long
using namespace std;
long long a[39]={
1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002
};
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("c.out","w",stdout);
	
	int task=0, CASE=0;
	long long A, B;
	for (scanf("%d", &task); task--;){
		scanf("%lld%lld", &A, &B);
		int ret = 0;
		for (int i=0; i<39; i++)
		if ( A<=a[i]*a[i] && a[i]*a[i]<=B )
			ret ++;
		printf("Case #%d: %d\n", ++CASE, ret);
	}
	return 0;
}

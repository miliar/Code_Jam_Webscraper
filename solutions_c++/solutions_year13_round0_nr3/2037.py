/*
 * By Duck
 */

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

long long A, B;
char a[100]; int dig;
int tal = 48;
long long par[100] = {
         1
,          4
,          9
,        121
,        484
,      10201
,      12321
,      14641
,      40804
,      44944
,    1002001
,    1234321
,    4008004
,  100020001
,  102030201
,  104060401
,  121242121
,  123454321ll
,  125686521ll
,  400080004ll
,  404090404ll
, 10000200001ll
, 10221412201ll
, 12102420121ll
, 12345654321ll
, 40000800004ll
, 1000002000001ll
, 1002003002001ll
, 1004006004001ll
, 1020304030201ll
, 1022325232201ll
, 1024348434201ll
, 1210024200121ll
, 1212225222121ll
, 1214428244121ll
, 1232346432321ll
, 1234567654321ll
, 4000008000004ll
, 4004009004004ll
, 100000020000001ll
, 100220141022001ll
, 102012040210201ll
, 102234363432201ll
, 121000242000121ll
, 121242363242121ll
, 123212464212321ll
, 123456787654321ll
, 400000080000004ll
};

int isp(long long n) {
	dig = 0;
	while( n ) { a[dig]=n%10; dig++; n/=10; }
	for( int i=0; i<dig/2; i++ )
		if( a[i]!=a[dig-i-1] )
			return 0;
	return 1;
}

int main(){
	int t, cnt;
	scanf("%d", &t);
	for( int r=1; r<=t; r++ ) {
		printf("Case #%d: ", r);
		scanf("%I64d %I64d", &A, &B);
		cnt = 0;
		for( int i=0; i<tal; i++ )
			if( A<=par[i] && par[i]<=B )
				cnt++;
		printf("%d\n", cnt);
	}
}


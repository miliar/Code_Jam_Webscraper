#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<cmath>
#include<map>
#define _USE_MATH_DEFINES
using namespace std;

int main() {
	unsigned long long palin[50];
	palin[0] = 1;
	palin[1] = 4;
	palin[2] = 9;
	palin[3] = 121;
	palin[4] = 484;
	palin[5] = 10201;
	palin[6] = 12321;
	palin[7] = 14641;
	palin[8] = 40804;
	palin[9] = 44944;
	palin[10] = 1002001;
	palin[11] = 1234321;
	palin[12] = 4008004;
	palin[13] = 100020001;
	palin[14] = 102030201;
	palin[15] = 104060401;
	palin[16] = 121242121;
	palin[17] = 123454321;
	palin[18] = 125686521;
	palin[19] = 400080004;
	palin[20] = 404090404;
	palin[21] = 10000200001;
	palin[22] = 10221412201;
	palin[23] = 12102420121;
	palin[24] = 12345654321;
	palin[25] = 40000800004;
	palin[26] = 1000002000001;
	palin[27] = 1002003002001;
	palin[28] = 1004006004001;
	palin[29] = 1020304030201;
	palin[30] = 1022325232201;
	palin[31] = 1024348434201;
	palin[32] = 1210024200121;
	palin[33] = 1212225222121;
	palin[34] = 1214428244121;
	palin[35] = 1232346432321;
	palin[36] = 1234567654321;
	palin[37] = 4000008000004;
	palin[38] = 4004009004004;
	palin[39] = 100000020000001;
	palin[40] = 100220141022001;
	palin[41] = 102012040210201;
	palin[42] = 102234363432201;
	palin[43] = 121000242000121;
	palin[44] = 121242363242121;
	palin[45] = 123212464212321;
	palin[46] = 123456787654321;
	palin[47] = 400000080000004;

	int t;
	unsigned long long A,B;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%llu %llu", &A, &B);
		int l, r;
		for (l = 0; A > palin[l]; l++) {}
		for (r = 39; B < palin[r]; r--) {}
		printf("Case #%d: %d\n", i+1, r-l+1);
	}
	return 0;
}

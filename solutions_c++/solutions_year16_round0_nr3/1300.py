#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

typedef long long LL;
const int mo[4] = {2,3,5,7};

LL n,J,tot;
int ans[20];

void PRINT(LL x)
{
	if (x == 1) {printf("1"); return;}
	PRINT(x>>1);
	if (x & 1) printf("1");
	else printf("0");
}

bool Judge(LL x,LL y,LL p)
{
	LL ret = 0,now = 1;
	for (; x; x >>= 1) {
		if (x&1) ret = (ret + now)%p;
		now = now*y%p;
	}
	return ret == 0;
}

int main()
{
	#ifdef YZY
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	
	int t; printf("Case #1:\n");
	cin >> t >> n >> J;
	for (LL i = 0; tot != J; i++) {
		int flag = 1;
		LL now = (i<<1LL) + 1LL + (1LL << (n-1LL));
		for (int j = 2; j <= 10; j++) {
			bool bo = 0;
			for (int l = 0; l < 4; l++) 
				if (Judge(now,j,mo[l])) {bo = 1; ans[j] = mo[l]; break;}
			if (!bo) {flag = 0; break;}
		}
		if (flag) {
			++tot; PRINT(now); printf(" ");
			for (int j = 2; j <= 10; j++) printf("%d ",ans[j]);
			printf("\n");
		}
	}	
	return 0;
}


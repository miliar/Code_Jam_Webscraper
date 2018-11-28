#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007

long long getLL() {
	long long ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

int getInt() {
	int ret = 0;
	char c;
	while (1) {
		c = getchar();
		if (c >= '0' && c <= '9') break ;
	}
	while (1) {
		ret = ret * 10 + c - '0';
		c = getchar();
		if (c < '0' || c > '9') break ;
	}
	return ret;
}

int n;
PII A[MaxN], B[MaxN], tmp[MaxN];
int main() {
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		scanf("%d", &n);
		For(i,1,n) scanf("%d", &A[i].FI);
		For(i,1,n) scanf("%d", &A[i].SE);
		int fir = true;
		while (1) {
			sort(A + 1, A + n + 1);
			if (n == 1 && A[1].SE == 1) break ;
			if (!fir) putchar(' ');
			fir = false ;
			if (A[1].SE > 1) {
				printf("0");
				For(i,1,n) A[i].SE /= 2;
				continue ;
			}
			int c = A[2].FI;
			printf("%d", c);
			int tot = 0, p = 0;
			int bn = 0;
			For(i,1,n) {
				while (p < tot && tmp[p + 1].FI == A[i].FI) {
					A[i].SE -= tmp[p + 1].SE;
					++p;
				}
				if (A[i].SE > 0) {
					B[++bn] = A[i];
					tmp[++tot] = {A[i].FI + c, A[i].SE};
				}
			}
			n = bn;
			For(i,1,n) A[i] = B[i];
		}
		puts("");
	}
	return 0;
}


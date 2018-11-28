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

long double getDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

int n;
long double V, X;
long double r[233], c[233];
pair<long double, long double> A[233];
int main() {
	//freopen("B-small-attempt0.in","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		scanf("%d", &n);
		V = getDouble(); X = getDouble();
		X *= V;
		For(i,1,n) r[i] = getDouble(), c[i] = getDouble();
		long double L = 0, R = 1e10;
		For(TIME,1,200) {
			long double mid = (L + R) / 2.0;
			For(i,1,n) A[i] = make_pair(c[i], r[i] * mid);
			sort(A + 1, A + n + 1);
			long double sum = 0;
			For(i,1,n) {
				sum += A[i].second;
			}
			if (sum < V) {
				L = mid; continue ;
			}
			long double Min = 0, cur = 0;
			For(i,1,n) {
				long double inc = min(A[i].second, V - cur);
				Min += inc * A[i].first;
				cur += inc;
			}
			reverse(A + 1, A + n + 1);
			long double Max = 0; cur = 0;
			For(i,1,n) {
				double inc = min(A[i].second, V - cur);
				Max += inc * A[i].first;
				cur += inc;
			}
			if ((X - Min) / X >= -1e-12 && (Max - X) / X >= -1e-12) R = mid; else L = mid;
		}
		if (L >= 5e9) puts("IMPOSSIBLE");
		else printf("%.12f\n", (double)L);
	}
	return 0;
}


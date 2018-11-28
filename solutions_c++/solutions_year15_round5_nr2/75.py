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

int n, K, sum[1111], d[1111];
pair<int,int> A[1111];
int main() {
	//freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n >> K;
		For(i,1,n - K + 1) scanf("%d", &sum[i]);
		int all = sum[1];
		For(i,2,n - K + 1) d[i - 1] = sum[i] - sum[i - 1];
		int Max = 0;
		For(i,1,K) {
			int s = 0; A[i] = {0, 0};
			for (int j = i; j + K <= n; j += K) {
				s += d[j];
				A[i].first = min(A[i].first, s);
				A[i].second = max(A[i].second, s);
			}
			Max = max(Max, A[i].second - A[i].first);
		}
		int l = Max, r = 1e8;
		while (l < r) {
			int mid = (l + r) / 2;
			long long x = 0, y = 0;
			For(i,1,K) x -= A[i].first, y += mid - A[i].second;
			int maxK, minK;
			if (all <= x) maxK = -(x - all + K - 1) / K;
			else maxK = (all - x) / K;
			if (y <= all) minK = (all - y + K - 1) / K;
			else minK = -(y - all) / K;
			if (maxK >= minK) r = mid; else l = mid + 1;
		}
		cout << l << endl;
	}
	return 0;
}


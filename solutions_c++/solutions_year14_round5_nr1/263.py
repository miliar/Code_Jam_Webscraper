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

int n,p,q,r,s;
int A[MaxN];
long long S[MaxN];
int main() {
	freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TTT,1,T) {
		printf("Case #%d: ",TTT);
		cin >> n >> p >> q >> r >> s;
		long long sum = 0;
		For(i,1,n) {
			A[i] = ((long long)(i - 1) * p + q) % r + s;
			sum += A[i];
		}
		long long ans = (long long)1e18;
		int p = 0;
		For(i,1,n) {
			S[i] = S[i - 1] + A[i];
			while (max(S[i] - S[p],S[p]) >= max(S[i] - S[p + 1], S[p + 1]) && p < i) ++p;
			ans = min(ans, max(S[i] - S[p], max(sum - S[i], S[p])));
		}
		long double t = ans;
		printf("%.12lf\n",(double)(1. - t / sum));
	}
	return 0;
}


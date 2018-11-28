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

pair<long long, long long> A[MaxN];
int n;
int main() {
	freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TK,1,T) {
		cin >> n;
		int hiker = 0;
		For(i,1,n) {
			long long tn, th, tb;
			cin >> tn >> th >> tb;
			For(j,1,th) A[++hiker] = {(360LL - tn) * (tb + j - 1), 360LL * (tb + j - 1)};
		}
		sort(A + 1, A + hiker + 1);
		long long ans = hiker;
		For(i,1,hiker) {
			long long tans = hiker - i;
			For(j,1,i - 1) tans += (A[i].first - A[j].first) / A[j].second;
			ans = min(ans, tans);
		}
		printf("Case #%d: %d\n", TK, ans);
	}
	return 0;
}


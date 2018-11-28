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
#define MaxN 10203
#define MaxNode 1020304
#define MD 1000000007

int n,A[MaxN],conToLeft[MaxN],conToRight[MaxN];
int main() {
	freopen("input.txt","r",stdin); //reopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TTT,1,T) {
		printf("Case #%d: ",TTT);
		cin >> n;
		For(i,1,n) scanf("%d",&A[i]);
		Fill(conToLeft,0);
		Fill(conToRight,0);
		For(i,1,n) {
			For(j,1,i) if (A[j] > A[i]) ++conToLeft[i];
			For(j,i,n) if (A[i] < A[j]) ++conToRight[i];
		}
		int ans = 0;
		For(i,1,n) ans += min(conToLeft[i],conToRight[i]);
		cout << ans << endl;
	}
	return 0;
}


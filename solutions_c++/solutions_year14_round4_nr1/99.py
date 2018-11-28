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

int A[MaxN],del[MaxN];
int main() {
	freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TTT,1,T) {
		printf("Case #%d: ",TTT);
		int n,x;
		scanf("%d%d",&n,&x);
		For(i,1,n) scanf("%d",&A[i]);
		sort(A + 1,A + n + 1);
		Fill(del,0);
		int ans = n;
		int p = n;
		For(i,1,n) {
			while (A[i] + A[p] > x) --p;
			if (p > i) --ans,--p;

		}
		cout << ans << endl;
	}
	return 0;
}


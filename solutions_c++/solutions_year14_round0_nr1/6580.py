//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 100010

int		main(){
	int cas, tt = 0, n, m;
	int A[4][4], B[4][4];
	scanf("%d", &cas);
	while (cas --) {
		scanf("%d", &n);
		Rep(i, 4) Rep(j, 4) scanf("%d", &A[i][j]);
		scanf("%d", &m);
		Rep(i, 4) Rep(j, 4) scanf("%d", &B[i][j]);
		n --, m --;
		int ans = -1;
		Rep(i, 4) Rep(j, 4) {
			if (A[n][i] != B[m][j]) continue;
			if (ans == -1) ans = A[n][i];
			else ans = -2;
			break;
		}
		printf("Case #%d: ", ++tt);
		if (ans == -2) puts("Bad magician!");
		else if (ans == -1) puts("Volunteer cheated!");
		else printf("%d\n", ans);
	}
	return 0;
}

#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>
#include <stack>
#include <sstream>
//#include <strstream>

using namespace std;

#define N 1005
#define M 1000005
#define P 1005
#define INF  0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define LL  long long
#define ULL unsigned long long
#define MOD 1000000007

#define eps 1e-9
#define PI acos(-1.0)
#define MID ((l + r)/2)
#define lx (x<<1)
#define rx ((x<<1)|1)

#define ppi pair<int,int>
#define lowbit(x) (x&(-x))
#define REP(i,n) for(int i=0;i<n;i++ )
#define REP_1(i,n) for(int i=1;i<=n;i++ )
#define FOR(i, a, b) for (int i=a;i<b;++i)
#define DWN(i, b, a) for (int i=b-1;i>=a;--i)
#define FOR_1(i, a, b) for (int i=a;i<=b;++i)
#define DWN_1(i, b, a) for (int i=b;i>=a;--i)
#define RST(A) memset(A, 0, sizeof(A))
#define FLC(A, x) memset(A, x, sizeof(A))

char a[105];

int main(){

    //freopen("in.txt","r",stdin);
	int t;
	int cas = 0;
	
	scanf("%d",&t);

	while(t--){
		cas++;
		printf("Case #%d: ",cas );

		scanf("%s",a);
		int ans = 1;

		int n = strlen(a);
		REP_1(i,n-1){
			if(a[i] != a[i-1]){
				ans++;
			}
		}
		if(a[n-1] == '+') ans--;
		printf("%d\n",ans );

	}

    return 0;
}

























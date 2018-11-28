#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<queue>
#define FI(i,a, b) for(int i=a;i<=b;i++)
#define FD(i,a, b) for(int i=a;i>=b;i--)

#define CL(x, y) memset(x, y, sizeof(x))
#define INF 2000000000
#define N 10000
#define MAXE ?
#define ll long long
using namespace std;
int n, m, t;
int a[N];
int main(){
	scanf("%d", &t);
	FI(k, 1, t){
		scanf("%d", &n);
		int ma = 0;
		FI(i, 0, n - 1){
			scanf("%d", &a[i]);
			ma = max(ma, a[i]);
		}
		int ans = INF;
		FI(i, 1, ma){
			int tmp = 0;
			int m1 = 0, m2 = 0;
			FI(j, 0, n - 1){
				int t1 = 0, t2 = a[j];
				tmp += (t2 - 1) / i;
				if(t2 / i) m2 = i;
				else m2 = max(m2, t2);
				
			}
			//printf("i = %d %d+%d = %d\n", i, m2, tmp, m2 + tmp);
			//printf("m2 = %d i = %d\n", i);
			ans = min(ans, m2 + tmp);
		}
		printf("Case #%d: %d\n", k, ans);
	}
}

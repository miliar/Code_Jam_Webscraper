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
#define MAXN ?
#define MAXE ?
#define ll long long
using namespace std;
int n, m, t;
char s[10000];
int main(){
	scanf("%d", &t);
	FI(k, 1, t){
		scanf("%d%s", &n, s);
		FI(i, 0, n){
			int p = i, ans = 0;
			FI(j, 0, n){
				if(j > p) ans = 1, j += n + 1;
				else p += s[j] - '0';
			}
			if(!ans){
				printf("Case #%d: %d\n", k, i);
				i += n + 1000;
			}
		}
	}
}

#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
#define FOR(i,a,b) for(int i = (a); i <(b); ++i)
#define SET(x,v) memset(x,v,sizeof(x))
const int maxn = 16;
int n;
char arr[maxn];
int cach[1<<maxn];
int qu[1<<maxn];
int doit(int stat) {
	if(stat == 0) return 0;
	int& ret = cach[stat];
	if(ret != -1) return ret;
	ret = 1048576;

	return ret;
}
int main() {
	int T,e=0;
	scanf("%d",&T);
	while(T--) {
		scanf("%s",arr);
		n = strlen(arr);
		int stat = 0;
		FOR(i,0,n) {
			if(arr[i] == '-') stat += (1<<i);
		}
		SET(cach,-1);
		int front = 0, rear = 0;
		qu[rear++] = stat;
		cach[stat] = 0;
		for(;front<rear && cach[0]==-1;++front) {
			int x = qu[front];
			FOR(i,0,n) {
				int next = 0;	
				int k = 0;
				for(int j = i; j >=0; --j,k++) {
					if(x & (1<<j));
					else next += (1<<k);
				}
				for(int j=i+1; j<n;++j) {
					next += x & (1<<j);
				}
				if(cach[next] == -1) {
					qu[rear++] = next;
					cach[next] = cach[x]+1;
				}
			}
		}	
		printf("Case #%d: %d\n", ++e, cach[0]);
	}
	return 0;
}

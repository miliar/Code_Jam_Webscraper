#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FORS(i,s) for(int i=0;(s)[i];i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back
#define INF 1000000000

int n,x;
int a[111111];

int main() {	
int nt; scanf("%d", &nt); FOR(tt,1,nt+1){
	scanf("%d%d", &n, &x);
	FOR(i,0,n) scanf("%d", &a[i]);
	sort(a,a+n);
	int cm = n-1;
	int ans = 0;
	FOR(i,0,n){
		if(cm < i) break;
		while(cm > i && a[i] + a[cm] > x){
			cm--;
			ans++;
		}
		if(cm == i){
			ans++;
			break;
		}else{
			cm--;
			ans++;
		}
	}
	printf("Case #%d: ", tt);
	printf("%d\n", ans);

}	
return 0;
}



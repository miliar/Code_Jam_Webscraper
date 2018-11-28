#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define Rep(i,a) for(int i = 0; i < (a); i++)
#define rep(i,a,b) for(int i = (a); i <= (b); i++)//(a)!
#define dep(i,a,b) for(int i = (a); i >= (b); i--)
#define ab(a) ((a) > 0 ? (a) : -(a))
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back(a)
using namespace std;
typedef long long LL;
typedef unsigned long long uLL;
bool vis[11];
int cnt;
void work(){
	int n; scanf("%d",&n); if (n == 0) {printf("INSOMNIA\n"); return;}
	memset(vis, false, sizeof(vis)); cnt = 0;
	for(int t = n;;t += n){
		int k = t;
		while (k) {
			if (!vis[k % 10]) vis[k % 10] = 1, cnt++;
			k /= 10;
		}
		if (cnt == 10) {printf("%d\n",t);return;}
	}
}
int main(){
	int T; scanf("%d",&T);
	int t = 0;
	while (T--) {
		t++;
		printf("Case #%d: ",t);
		work();
	}
	return 0;
}
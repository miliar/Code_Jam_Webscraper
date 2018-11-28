#include <cstdio>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

#define getmid(l,r) ((l) + ((r) - (l)) / 2)
#define MEM(a,b) memset(a,b,sizeof(a))
#define MP(a,b) make_pair(a,b)
#define PB push_back

typedef long long ll;
typedef pair<int,int> pii;
const double eps = 1e-8;
const int INF = (1 << 30) - 1;
const int MAXN = 100010;

int T;
ll v,vv;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.txt","w",stdout);
	scanf("%d",&T);
	for(int tt = 1; tt <= T; ++tt){
		scanf("%lld",&vv);
		v = vv;
		printf("Case #%d: ",tt);
		if(v == 0){
			printf("INSOMNIA\n");
			continue;
		}
		int state = 0;
		int ans = 1;
		while(1){
			ll tv = v;
			while(tv){
				state |= (1 << (tv % 10));
				tv /= 10;
			}
			if(state == (1 << 10) - 1) break;
			ans++;
			v += vv;
		}
		printf("%lld\n",v);
	}
	return 0;
}
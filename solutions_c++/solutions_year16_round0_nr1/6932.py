#include <algorithm>
#include <iostream>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#define INF 0x3f3f3f3f
#define Mn 100010
#define Mm 200010
#define mod 1000000007
#define CLR(a,b) memset((a),(b),sizeof((a)))
#define CPY(a,b) memcpy ((a), (b), sizeof((a)))
#pragma comment(linker, "/STACK:102400000,102400000")
#define ul (u<<1)
#define ur (u<<1)|1
using namespace std;
typedef long long ll;
int vis[10];
void check(ll x) {
	while(x) {
		vis[x%10]=1;
		x/=10;
	}
}
int main() {
	freopen("A-large.in","r",stdin);
   	freopen("001.out","w",stdout);
	int t,cas=0;
	scanf("%d",&t);
	while(t--) {
		int n;
		cas++;
		scanf("%d",&n);
		printf("Case #%d: ",cas);
		if(n==0) {printf("INSOMNIA\n");continue;}
		ll x=0;
		CLR(vis,0);
		for(int i=1;;i++) {
			x+=n;
			check(x);
			int num=0;
			for(int j=0;j<10;j++) {
				if(vis[j]) num++;
			}
			if(num==10) break;
		}
		printf("%lld\n",x);
	}
    return 0;
}

/*  ^^ ====== ^^
ID: meixiuxiu
PROG: test
LANG: C++11
*/
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cctype>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int ,int> pii;
#define MEM(a,b) memset(a,b,sizeof a)
#define CLR(a) memset(a,0,sizeof a);
#define pi acos(-1.0)
#define maxn 40000
#define maxv 100005
const int inf = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
#define LOCAL
bool vis[11];
int main()
{
#ifdef LOCAL
	freopen("C:\\Users\\honm\\Desktop\\in.txt", "r", stdin);
	freopen("C:\\Users\\honm\\Desktop\\out.txt","w",stdout);
#endif
	int t;cin >> t;
	int kase = 1;
	while(t--){
		printf("Case #%d: ",kase++);
		int base;scanf("%d",&base);
		MEM(vis,0);
		int cnt = 0;
		if(base==0){
			printf("INSOMNIA\n");
		}
		else{
			int tmp = base;
			while(1){
				int x = tmp;
				while(x){
					if(!vis[x%10])vis[x%10]=1,cnt++;
					x/=10;
				}
				if(cnt==10)break;
				tmp += base;
			}
			printf("%d\n",tmp);
		}
	}
	return 0;
}











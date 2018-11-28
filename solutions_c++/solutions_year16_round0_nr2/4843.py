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
char s[110];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B.txt","w",stdout);
	scanf("%d",&T);
	for(int tt = 1; tt <= T; ++tt){
		scanf("%s",s + 1);
		int len = strlen(s + 1);
		int ans = 0;
		for(int i = len; i >= 1; --i){
			if(s[i] == '-'){
				for(int j = 1; j <= i; ++j){
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
				ans++;
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
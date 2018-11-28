#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cmath>
#include <ctime>
#include <iomanip>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <string>
using namespace std;

const int inf = 1000000005;
const int maxn=20000;
const int maxm = 200000 + 5;

int tot;
int tst, n, m, S, T;
int lay[maxn],cur[maxn],q[maxn];
int V[maxm],N[maxm],G[maxm],F[maxn];
vector<int> from[maxn];
map<string, int> bel;

void add(int a, int b, int f)  {
	++ tot, V[tot] = b, G[tot]=f,N[tot]=F[a],F[a]=tot;
	++tot,V[tot]=a,G[tot]=0,N[tot]=F[b],F[b]=tot;
}
bool bfs(int n){
     for (int i = 1; i <= n; i ++)
        lay[i] = n + 1, cur[i] = F[i];
     int hd = 0, tl = 1;
     q[1] = T, lay[T] = 0;
     while (hd != tl){
        int u = q[++ hd], v;
        for (int p = F[u]; p > 0; p = N[p])
           if (G[p ^ 1] > 0 && lay[v = V[p]] >= n){
               q[++ tl] = v;
               lay[v] = lay[u] + 1;
           }
     }
     return lay[S] < n;
}
int aug(int u,int f){
    if (u == T) return f;
    int rm = f, d;
    for (int &p = cur[u]; p > 0; p = N[p])
       if (G[p] > 0 && lay[V[p]] + 1 == lay[u]){
           d = aug(V[p], G[p] < rm ? G[p] : rm);
           G[p] -= d, G[p ^ 1] += d, rm -= d;
           if (rm == 0) return f;
       }
    return f - rm;
}
int dinic(int n){
     int ret = 0;
     while (bfs(n)) {
     	ret += aug(S, inf);
     	if (ret>=inf)return ret;
     }
     return ret;
}
int main()  {
	scanf("%d", &tst);
	n=m=0;
	for (int t = 1; t <= tst; t ++)  {
		for (int i=1;i<=tot;i++) N[i]=G[i]=V[i]=0;
		for (int i=1;i<=n+2*m+10;i++) F[i]=0;
		tot=1;

		scanf("%d", &n);
		m = 0;
		string tmp="";
		for (int i = 1; i <= n; i ++)  {
			tmp="";
			char c=getchar();
			while (c < 'a' || c > 'z') c = getchar();
			while (c!='\n') {
				while (c<'a'||c>'z')c=getchar();
				tmp="";
				while (c >= 'a' && c <= 'z')  {
					tmp = tmp + c;
					c = getchar();
				}
			//	cout <<"sentence " << i << " word = " << tmp <<endl;

				if (!bel.count(tmp)) bel[tmp] = ++ m;
				from[bel[tmp]].push_back(i);
			}
		}

		S = n + 2 * m + 1, T = S + 1;
		for (int i = 1; i <= m; i ++)  { //S-ENG, T-FRENCH
			int x = i + n, y = i + n + m;
			add(S, x, 1), add(y, T, 1);
			for (int j = 0; j < (int)from[i].size(); j ++)  {
				add(x, from[i][j], inf);
				
			}
			for (int j = 0; j < (int)from[i].size(); j ++)
				add(from[i][j], y, inf);
		}
		add(S, 1, inf), add(2, T, inf);
		printf("Case #%d: %d\n", t, dinic(T) - m);
		for (int i=1;i<=m;i++) from[i].clear();
		bel.clear();
	}
	return 0;
}
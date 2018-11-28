#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <utility>
#include <stack>
#include <iostream>

using namespace std;

int n;
typedef long long ll;
typedef __int128 int128;

int ent[105], sai[105];
ll mod = 1000002013;
int ret[105];
int total[105];
int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	int t,m;
	ret[1] = 1;
	for(int i = 2; i < 104; ++i) ret[i] = ret[i-1]+i;
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		printf("Case #%d: ", _);
		scanf("%d %d", &n, &m);
		ll custo = 0;
		ll resp = 0;
		memset(total, 0, sizeof total);
		memset(ent, 0, sizeof ent);
		memset(sai, 0, sizeof sai);
		for(int i = 0; i < m; ++i){
			int a, b, c;
			scanf("%d %d %d", &a, &b, &c);
			ent[a] += c;
			sai[b] += c;
			custo += ((b-a)*n - ret[b-a-1])*c;
		}
		for(int i = 1; i <= n; ++i){
			for(int j = n; j > 0; --j)
				total[j] = total[j-1];
			total[0] = ent[i];
			int falta = sai[i];
			int at = 0;
			while(falta){
				if(!total[at]) at++;
				else{
					total[at]--;
					falta--;
					resp += at*n - ret[at-1];
					//printf("adicionando custo %lld (saindo no %d, entrou em %d)\n", at*n - ret[at-1], i, i-at);
				}
			}
		}
		//printf("custo %lld  resp %lld\n", custo, resp);
		resp = (custo-resp+mod)%mod;
		printf("%lld\n", resp);
	}
	return 0;
}

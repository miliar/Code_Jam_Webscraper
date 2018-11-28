#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <iostream>
#include <sstream>

using namespace std;

const int N = 2e5;

map<unsigned long long , int >my;

int q[210][1100], f[210];
char s[N];
int all[N];
int tt;
int main()
{
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		my.clear();
		int cnt = 0;
		int n;
		scanf("%d", &n);
		gets(s);
		for(int i=0; i<n; ++i){
			f[i] = 0;
			gets(s);
			int l = strlen(s);
			assert(l > 0 && l < N);
			int star = 0;
			while(star < l){
				while(star < l && !islower(s[star])) ++star;
				if(star >= l) break;
				int e = star + 1;
				while(e < l && islower(s[e])) ++e;
				unsigned long long hash = 0;
				for(int j = star; j < e; ++j){
					hash = hash * 29 + (s[j] - 'a'+1);
				}
				if(my.find(hash) == my.end()){
					my[hash] = ++cnt;
					all[cnt] = 0;
				}
				{
					tt = my[hash];
					q[i][f[i]++] = tt;
					all[tt] |= (1<<i);
				}
				star = e;
			}
		}
		int ans = N;
		int upp = (1<<n);
		for(int i=1, other = upp - 2; i<upp; i+=4, other -= 4){ 
/*			fen = 0;
			ffa = 0;
			for(int j=0; j<n; ++j){
				int t;
				if((1<<j) & i){
					for(int k = 0; k < f[j]; ++k)
						en[fen++] = q[j][k];
				}else{
					for(int k = 0; k < f[j]; ++k)
						fa[ffa++] = q[j][k]; 
				}
			}
			sort(en, en + fen);
			sort(fa, fa + ffa);
			{
				int tf = 1;
				for(int i=1; i<fen; ++i){
					if(en[i] != en[i-1]){
						en[tf++] = en[i];
					}
				}
				fen = tf;
			}
			{
				int tf = 1;
				for(int i=1; i<ffa; ++i){
					if(fa[i] != fa[i-1]){
						fa[tf++] = fa[i];
					}
				}
			}
			int tot = 0;
			int t1 = 0, t2 = 0;
			while(t1 < fen && t2 < ffa){
				if(en[t1] < fa[t2]){
					++t1;
				}else if(en[t1] > fa[t2]){
					++t2;
				}else {
					++t1, ++t2;
					++tot;
				}
			}
			ans = min(ans, tot);*/
			int tot = 0;
			for(int j=1; j<=cnt; ++j){
				if((all[j] & other) && (all[j] & i))tot ++;
			}
			ans = min(ans, tot);
		}
		printf("Case #%d: %d\n", cc, ans);
	}
	return 0;
}


#include <cstdio>
#include <algorithm>
#include <vector>
#define N 100005
#define fi(a, b, c) for(int a = (b); a < (c); a++)
#define fd(a, b, c) for(int a = (b); a > (c); a--)
#define FI(a, b, c) for(int a = (b); a <= (c); a++)
#define FD(a, b, c) for(int a = (b); a >= (c); a--)
#define fe(a, b, c) for(int a = (b); a; a = c[a])
using namespace std;

int tc, n, t[N][26], p, w[N], cw, ans, base, wl[N], len;
char s[N];
vector<int> v[N];
bool e[N], f[N], e2[N], f2[N];

void init(int x){
	fi(i, 0, 26) t[x][i] = 0;
	w[x] = 0;
}

void solve(int tt){
	scanf("%d", &n);
	p = cw = 0;
	init(0);
	
	fi(i, 0, n){
		v[i].clear();
		scanf("\n%[^\n]", s);
		for(int j = 0; s[j]; j++){
			int k = j, r = 0;
			while(s[k] && s[k] != ' '){
				if(!t[r][s[k] - 'a']){
					t[r][s[k] - 'a'] = ++p;
					init(p);
				}
				r = t[r][s[k] - 'a'];
				k++;
			}
			if(!w[r]) w[r] = ++cw;
			v[i].push_back(w[r]);
			
			if(!s[k]) break;
			j = k;
		}
	}
	
	base = 0;
	FI(i, 1, cw) e[i] = f[i] = e2[i] = f2[i] = 0;
	fi(i, 0, v[0].size()) e[v[0][i]] = 1;
	fi(i, 0, v[1].size()) f[v[1][i]] = 1;
	FI(i, 1, cw) base += f[i] * e[i];
	
	len = 0;
	fi(i, 2, n) fi(j, 0, v[i].size()) wl[len++] = v[i][j];
	sort(wl, wl + len);
	len = unique(wl, wl + len) - wl;
	
	ans = N;
	fi(i, 0, 1 << (n - 2)){
		fi(j, 0, len) f2[wl[j]] = e2[wl[j]] = 0;
		fi(j, 2, n){
			if(i & 1 << (j - 2)){
				fi(k, 0, v[j].size()) f2[v[j][k]] = 1;
			}else{
				fi(k, 0, v[j].size()) e2[v[j][k]] = 1;
			}
		}
		
		int cnt = base;
		fi(j, 0, len){
			int x = wl[j];
			if(f[x] && e[x]) continue;
			if((f2[x] || f[x]) && (e2[x] || e[x])) cnt++;
		}
		
		ans = min(ans, cnt); 
	}
	
	printf("Case #%d: %d\n", tt, ans);
}

int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w+", stdout);
	scanf("%d", &tc);
	FI(z, 1, tc) solve(z);
	scanf("\n");
}

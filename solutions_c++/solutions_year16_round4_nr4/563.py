#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = 30, mod = int(1e9)  + 7;
int T;
int p[N],a[N];
int ok[N][N],n,c[N][N];
char s[N][N];
bool bad,f;

void rec(int v){
	if(bad) return;
	if(v == n + 1){
		return;	       	
	}
	for(int i=0;i<n;i++) if(p[i] == -1){
		p[i] = v;
		bool f = 0;
		for(int j=0;j<n;j++) if(c[i][j] && a[j] == -1){
			a[j] = i;
			rec(v+1);
			f = 1;
			a[j] = -1;
		}
		if(!f){
			bad = 1;
			return;
		}
		p[i] = -1;
	}
}

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		scanf("%d\n",&n);
		int ans = mod;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				cin >> s[i][j];
				ok[i][j] = s[i][j] - '0';
			}
		}
		for(int mask=0;mask<(1<<(n*n));mask++){
			int res = __builtin_popcount(mask);
			bool ff = 0;
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++) 
					if(mask & (1<<(i*n+j))){
						if(!ok[i][j]){
							c[i][j] = 1;
						}
						else {
						    ff = 1;
						    break;
						}
					}
					else c[i][j] = ok[i][j];
			}
			if(ff) continue;
			bad = 0;
			memset(p,-1,sizeof(p));
			memset(a,-1,sizeof(a));
			rec(1);
			if(!bad) ans = min(ans,res);
		}
		cout <<ans << endl;
	}

return 0;
}
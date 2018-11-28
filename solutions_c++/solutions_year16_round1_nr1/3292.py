#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <set>
#include <limits>
using namespace std;

#define FOR(i,f,t) for(int i=f; i<t; i++)
#define ms(obj, val) memset(obj, val, sizeof(obj))
#define pb push_back
#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d %d", &x, &y)
#define SYNC ios_base::sync_with_stdio(false)

typedef long long ll;

#define MAXN 1500

int k, N;
char S[MAXN], ans[MAXN];
bool used[MAXN];


void solve(int r){
	if(r==-1) return;
	char maxi=0; int oc;
	FOR(i, 0, r+1)
		if(maxi < S[i]){
			maxi = S[i];
			oc = i;
		}
	FOR(i, oc, r+1)
		if(S[i] == maxi){
			ans[k++] = S[i];
			used[i] = true;
		}
	solve(oc-1);
	FOR(i,oc,r+1) if(!used[i]) ans[k++] = S[i];
}


int main(){
	int TC; ri(TC);
	FOR(tc,0,TC){
		ms(ans,0); ms(S, 0);
		ms(used, false);
		scanf("%s",S);
		N = strlen(S);
		k = 0;
		solve(N-1);
		printf("Case #%d: %s\n",tc+1, ans);
	}
}


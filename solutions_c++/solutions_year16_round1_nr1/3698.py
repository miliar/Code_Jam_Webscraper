#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <iostream>
#include <set>
#include <cmath>
#include <cassert>
#include <ctime>
#include <string>

using namespace std;

#define db(x) cout << #x " == " << x << endl
#define _ << ", " <<
#define fr(a,b,c) for(int a = b; a < c; a++)
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = ant[b]; ~a; a = ant[a])
#define cl(a,b) memset(a,b,sizeof(a))

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define add_edge(a,b) to[z] = b; ant[z] = adj[a]; adj[a] = z; z++
#define oo 0x3f3f3f3f
#define EPS 1e-8
#define MOD 1000000007

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<int, pii> dist_pos;
typedef pair<ll, ll> pll;
typedef pair<int, char> pic;
typedef pair<double, int> pdi;

int T, N;
char ar[10010];
int maxi[10010];
int len;
char ans[10010];

void resolve(int rightEnd){
	if(rightEnd == 0) ans[len++] = ar[rightEnd];
	else{
		int posM = maxi[rightEnd];
		ans[len++] = ar[posM];
		if(posM-1 >= 0) resolve(posM-1);
		fr(i, posM+1, rightEnd+1)
			ans[len++] = ar[i];
	}
}

int main(){
	scanf("%d", &T);
	rp(t, T){
		len = 0;
		memset(ans, 0, sizeof(ans));
		scanf("%s", ar);
		maxi[0] = 0;
		N = strlen(ar);
		fr(n, 1, N){
			maxi[n] = maxi[n-1];
			if(ar[n] >= ar[maxi[n]]) maxi[n] = n;
		}
		resolve(N-1);
		printf("Case #%d: %s\n", t+1, ans);
	}
}

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

int T;
bool mark[10];
long long num;

long long solve(long long num){
	if(num == 0) return -1;
	long long cur = num;
	int mult = 1;
	while(true){
		cur = num*mult;
		while(cur != 0){
			if(!mark[cur%10]){
				mark[cur%10] = true;
			}
			cur /= 10;
		}
		bool toCont = false;
		rp(i, 10) if(!mark[i]) toCont = true;
		if(!toCont) break;
		mult++;
	}
	rp(i, 10) if(!mark[i]) return -1;
	return num*(mult);
}

int main(){
	scanf("%d", &T);
	rp(t, T){
		scanf("%lld", &num);
		memset(mark, 0, sizeof(mark));
		ll ans = solve(num);
		printf("Case #%d: ", t+1);
		if(ans== -1) printf("INSOMNIA\n");
		else printf("%lld\n", ans);
	}
}

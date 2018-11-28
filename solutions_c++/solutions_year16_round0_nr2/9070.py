#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define ll long long

#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 110
#define MOD 1000000007

using namespace std;

char s[MAX];
int sz;

void print(int n){
	rep(i, sz) printf("%c", (1<<i)&n ? '+' : '-');
	puts("");
}

int flip(int n, int end){
	bool v[10];
	rep(i, sz) v[i] = (1<<i)&n ? 1 : 0;
	for(int i = 0; i<=end; i++) v[i] ^= 1;
	for(int i = 0, j = end; i < j; i++, j--) swap(v[i], v[j]);
	
	int ans = 0;
	rep(i, sz) if(v[i]) ans |= 1<<i;
	
	return ans;
}

typedef pair<int, int> pii;

set<int> v;
map<int, int> dp;

int solve(int s, int k){

	queue<pii> q;
	q.push(pii(s, 0));
	
	while(!q.empty()){
		int atual = q.front().first;
		int dist = q.front().second;
		q.pop();
		
		// rep(i, dist) putchar('\t'); print(atual);
		
		if(atual+1 == 1<<sz) return dist;
		if(v.count(atual) > 0) continue;
		v.insert(atual);
		
		rep(i, sz) q.push(pii(flip(atual, i), dist+1));
	}
	
	return -1;
}

int main (){
	int n;
	scanf("%d", &n);
	
	rep(T, n){
		v.clear();
		scanf("%s", s);
		sz = strlen(s);
		
		int num = 0;
		rep(i, sz) if(s[i] == '+') num |= 1<<i;
		int ans = solve(num, 0);
		printf("Case #%d: %d\n", T+1, ans);
		
	}

	return 0;
}

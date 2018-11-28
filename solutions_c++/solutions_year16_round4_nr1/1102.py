#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;

typedef long long ll;
#define pb push_back

int cnt[3], n, R, P, S;
string node[20000] = {};

void build(int x, int o){
	if(o >= (1<<(n+1))) {
		return;
	}
	//node[o] = x;
	// cout << o << ' ' << x <<endl; 
	if(o >= (1<<n)) {
		if(!x) node[o] = 'R';
		else if(x == 1) node[o] = 'P';
		else node[o] = 'S';
		++cnt[x];
	}
	int le, ri;
	le = x;
	ri = (x+2)%3;
	build(ri, o<<1|1);
	build(le, o<<1);
}

void cal(int o){
	if(o >= (1<<n)) return;
	cal(o<<1);
	cal(o<<1|1);
	if(node[o<<1] > node[o<<1|1])
		node[o] = node[o<<1|1] + node[o<<1];
	else node[o] = node[o<<1] + node[o<<1|1];
}

int main () {
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++){
		for(int i = 0; i < 5000; ++i) node[i] = "";
		cin >> n;
		cin >> R >> P >> S;
		int ok = 0;
		for(int i = 0; i < 3 && !ok; ++i){
			memset(cnt, 0, sizeof(cnt));
			build(i, 1);
			if(cnt[0] == R && cnt[1] == P && cnt[2] == S)ok = 1;
		}
		// for(int i = 0; i < 8; ++i) cout << node[i] << ' ' ; cout <<endl;
		printf("Case #%d: ", tt);
		if(!ok){
			puts("IMPOSSIBLE");
		}
		else{
			cal(1);
			cout<< node[1] <<endl;
		}
	}
}
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

int N;
bool k[5][5], nk[5][5];
int cost = 0;
int ans = 10000000;
vector<int> v;
bool used[5];

bool check(int p=0){
	if(p==N) return true;
	int cnt=0;
	FOR(i,0,N) if(nk[v[p]][i] && !used[i]) cnt++;
	if(cnt == 0) return false;
	bool good = true;
	FOR(i,0,N) if(nk[v[p]][i] && !used[i]){
		used[i] = true;
		if(!check(p+1)) good = false;
		used[i] = false;
	}
	return good;
}

void check_all(){
	v.clear();
	FOR(i,0,N) v.pb(i);
	bool good = true;
	do{
		ms(used,false);
		if(!check()){
			good = false;
		}
	}while(next_permutation(v.begin(), v.end()));
	if(good){
		ans = min(ans, cost);
	}
}

void bt1(int p=0, int t=0){
	if(t==N){
		if(p==N-1){
			check_all();
		}else{
			bt1(p+1, 0);
		}
		return;
	}
	bt1(p, t+1);
	if(!k[p][t]){
		cost++;
		nk[p][t] = 1;
		bt1(p,t+1);
		nk[p][t] = 0;
		cost--;
	}
}

int main(){
	int TC; ri(TC);
	FOR(tc,1,TC+1){
		ri(N);
		FOR(i,0,N){
			char line[10]; scanf("%s",line);
			FOR(j,0,N) if(line[j]=='0') k[i][j] = 0;
						else			k[i][j] = 1;
		}
		FOR(i,0,N) FOR(j,0,N) nk[i][j] = k[i][j];
		ans = 100000000;
		cost = 0;
		bt1();
		printf("Case #%d: %d\n",tc,ans);
	}
}


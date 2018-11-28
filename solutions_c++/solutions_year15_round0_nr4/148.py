#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define RI(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const ll INF = (ll) inf * inf;
const int nax = 5e6 + 5;

bool te() {
	int x, a, b;
	scanf("%d%d%d", &x, &a, &b);
	if(a > b) swap(a, b);
	if(a * b % x != 0) return false;
	if(x >= 7) return false;
	if(x > max(a,b)) return false;
	if(x >= 2 * min(a, b) + 1) return false;
	if(x == 4 && a == 2 && b == 4) return false;
	if(x == 5 && a == 3 && b == 5) return false;
	if(x == 6 && a == 3) return false;
	
	return true;
}

#include<iostream>
int main(int argc, char *argv[])
{
	debug = argc > 1;
	
	int T;
	scanf("%d", &T);
	RI(test, T) {
		printf("Case #%d: ", test);
		puts(te() ? "GABRIEL" : "RICHARD");
	}
	
	return 0;
}

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
char con[110];

int solve(){
	int counter = 0;
	int len = strlen(con);
	int point = 0;
	bool type = (con[0] == '+');
	rp(i, len){
		if(type && con[i] == '+') point++;
		else if(type) break;
		else if(con[i] == '-') point++;
		else break;
	}
	while(point < len){
		counter++;
		rp(i, point){
			if(type) con[i] = '-';
			else con[i] = '+';
		}
		type = !type;
		while(point < len && ((type && con[point] == '+') || (!type && con[point] == '-')))
			point++;
	}
	if(con[len-1] == '+') return counter;
	else return counter+1;
}

int main(){
	scanf("%d", &T);
	rp(t, T){
		printf("Case #%d: ", t+1);
		scanf("%s", con);
		printf("%d\n", solve());
	}
}

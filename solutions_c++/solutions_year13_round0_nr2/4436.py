#include <stdio.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <memory.h>
#include <map>
#include <vector>
#include <set>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define repk(i,a,b) rep(i,a,(b)-1)
#define rrep(i,a,b) for(int i=(b);i>=(a);i--)
#define rrepk(i,a,b) rrep(i,a,(b)-1)
#define fe(e,x) for(edge *e = (x)->first;e;e = e->next)
#define foreach(tank_type,iterator_name,set_name) \
	for(tank_type::iterator iterator_name = (set_name).begin();iterator_name != (set_name).end();iterator_name++)
#define comp_def(cmp_name,type) bool cmp_name(type l,type r)
#define ifn(x) if(!(x))
#define vind(p_point) (p_point-points)
#define eind(p_edge) (p_edge-edges)
#define eopp(p_edge) (edges+(eind(p_edge)^1))
#define mp(x,y) make_pair((x),(y))
#define OIFILE(filename) freopen(filename##".in","r",stdin);freopen(filename##".out","w",stdout)
#define OICLOSE fclose(stdin);fclose(stdout)
typedef long long ll;
const int inf = 0x3fffffff,upinf = 0x7fffffff,geps = 10;
const double eps = 1e-12,dinf = 1e20;

const int maxn = 1000;
int height[maxn][maxn];
int rowmax[maxn],colmax[maxn];

int n,m;
void Init(){
	scanf("%d%d",&n,&m);
	repk(i,0,n) repk(j,0,m) scanf("%d",height[i]+j);
	repk(i,0,n){
		rowmax[i] = -inf;
		repk(j,0,m) rowmax[i] = max(rowmax[i],height[i][j]);
	}repk(j,0,m){
		colmax[j] = -inf;
		repk(i,0,n) colmax[j] = max(colmax[j],height[i][j]);
	}
}

void solve(int case_ind){
	printf("Case #%d: ",case_ind);
	repk(i,0,n) repk(j,0,m){
		if(height[i][j] != min(rowmax[i],colmax[j])){
			printf("NO\n");
			return;
		}
	}printf("YES\n");
}

int main(){
#ifndef ONLINE_JUDGE
	OIFILE("B");
#endif

	int t;scanf("%d",&t);
	rep(i,1,t){
		Init();
		solve(i);
	}

#ifndef ONLINE_JUDGE
	OICLOSE;
#endif
	return 0;
}

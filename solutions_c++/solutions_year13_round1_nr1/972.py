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
const ll llinf = 0x3fffffffffffffffll;

ll r,t;
void Init(){
	scanf("%I64d%I64d",&r,&t);
}

bool check(ll n){
	double x = 2.0*double(n)*double(n)+(2.0*double(r)-1.0)*double(n);
	if(x > llinf) return true;
	else return 2*n*n+(2*r-1)*n > t;
}

void solve(int cases){
	printf("Case #%d: ",cases);
	ll L = 1,R = t;
	for(ll mid = (L+R)>>1;L<=R;mid = (L+R)>>1)
		check(mid)?R = mid-1:L = mid+1;
	printf("%I64d\n",R);
}

int main(){
#ifndef ONLINE_JUDGE
	OIFILE("A");
#endif

	int T;scanf("%d",&T);
	rep(i,1,T){
		Init();
		solve(i);
	}

#ifndef ONLINE_JUDGE
	OICLOSE;
#endif
	return 0;
}

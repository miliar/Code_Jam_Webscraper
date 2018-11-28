/* hanhanw v1.2 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
// for Online Judge or Contests
#define MSET(x,y) memset(x,y,sizeof(x))
#define REP(x,y,z) for(int x=(y); x<=(z); x++)
#define FORD(x,y,z) for(int x=(y); x>=(z); x--)
#define FLST(x,y,z) for(int x=(y); x; x=z[x])
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define SZ(x) ((int)x.size())
#define PB push_back

using namespace std;
//
typedef long long LL;
typedef unsigned long long uLL;
typedef long double LD;
// start here OAO~

const int M = 2048;

const LL MOD = 1000002013;

int top,m;
LL n,yuan;
pair<LL,LL> in[M],stk[M];

bool comp(pair<LL, LL> a, pair<LL, LL> b){
	if (a.first != b.first) return a.first < b.first;
	return a.second > b.second;
}
inline LL calc(LL st, LL ed, LL p){
	LL a,b;
	a=ed-st;
	b=2ll*n-(ed-st-1);
	if (a % 2 == 0) a /= 2ll;
	else b /= 2ll;
	return (a%MOD) * (b%MOD) % MOD * p % MOD;
}
void input(){
	yuan = 0;
	scanf("%I64d %d", &n, &m);
	for (int i=1; i<=m; i++){
		LL st,ed,p;
		scanf("%I64d %I64d %I64d", &st, &ed, &p);
		p %= MOD;
		in[i] = make_pair(st,p);
		in[i+m] = make_pair(ed,-p);

		yuan += calc(st,ed,p);
	}
	sort(in+1,in+1+2*m,comp);
}
void solve(int T){
	input();
	top=0;
	LL res=0;
	for (int i=1; i<=2*m; i++){
		if (in[i].second > 0){
			stk[top++] = make_pair(in[i].first, in[i].second);
		} else {
			LL p=in[i].second * -1;
			while (top && p){
				if (stk[top-1].second <= p){
					res = (res + calc(stk[top-1].first,in[i].first,stk[top-1].second)) % MOD;
					p -= stk[top-1].second;
					top--;
				} else {
					res = (res + calc(stk[top-1].first,in[i].first,p)) % MOD;
					stk[top-1].second -= p;
					p = 0;
				}
			}
		}
	}
	res = ((yuan-res)%MOD+MOD)%MOD;
	printf("Case #%d: %I64d\n", T, res);
}
int main(int argc, char** argv){
	int nT; scanf("%d", &nT);
	for (int i=1; i<=nT; i++)
		solve(i);

	return 0;
}

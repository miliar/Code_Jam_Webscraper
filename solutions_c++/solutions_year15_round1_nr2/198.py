#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <cstring>
using namespace std;
#define rep(i,a,b) for(int i = (a);i<=(b);i++)
#define repk(i,a,b) rep(i,(a),(b)-1)
#define rrep(i,a,b) for(int i = (b);i>=(a);i--)
#define rrepk(i,a,b) rrep(i,(a),(b)-1)
const int inf = 0x3fffffff,dinf = 0x7fffffff,geps = 10;
typedef long long ll;

const int maxb = 1000;
int B,N;
int ary[maxb + geps];
int maxM;
void Init(){
	scanf("%d%d",&B,&N);
	maxM = 0;
	rep(i,1,B){
		scanf("%d",ary+i);
		maxM = max(maxM, ary[i]);
	}
}

ll updiv(ll a,ll b){
	return (a + b - 1) / b;
}
ll gettotal(ll mid){
	ll total = 0;
	rep(i,1,B){
		total += updiv(mid,ary[i]);
	}
	return total;
}
bool check(ll mid){
	//printf("Check %lld:", mid);
	ll total = gettotal(mid);
	//printf("%s\n", total < N ? "Yes" : "No");
	return total <= N - 1;
}

void solve(){
	ll l = 1, r = ll(maxM) * ll(N);
	for(ll mid = (l+r)>>1;l<=r;mid = (l+r)>>1)
		check(mid) ? l = mid + 1 : r = mid - 1;
	//printf("r : %lld\n",r);
	int cnt = N - int(gettotal(r));
	rep(i,1,B){
		if(r % ary[i] == 0){
			cnt--;
		}
		if(!cnt){
			printf("%d\n",i);
			return;
		}
	}
}

int main(){

	int Test;
	scanf("%d",&Test);
	for(int t = 0; t < Test; ++t){
		Init();
		printf("Case #%d: ", t+1);
		solve();
	}
	
	return 0;
}

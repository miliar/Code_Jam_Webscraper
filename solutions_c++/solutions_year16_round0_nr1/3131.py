#include <bits/stdc++.h>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
typedef long long ll;
const int maxn = 100005;
ofstream out("out.txt");

int vis[15];
int haha;
void fen(ll now){
	while(now){
		if(!vis[now % 10]){
			vis[now % 10] = 1;
			haha--;
		}
		now = now / 10;
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cas = 1;cas  <= T;cas++){
		ll n;
		scanf("%lld",&n);
		out<<"Case #"<<cas<<": ";
		if(n == 0){
			out<<"INSOMNIA\n";
			continue;
		}
		haha = 10;
		ll now;
		mem(vis,0);
		ll ans = 0;
		for(ll i = 1;haha > 0;i++){
			now = n * i;
			fen(now);
			ans = now;
		}
		out<<ans<<"\n";
	}
}

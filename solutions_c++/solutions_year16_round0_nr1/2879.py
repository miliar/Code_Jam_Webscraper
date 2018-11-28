#include<bits/stdc++.h>
#define MAXN 100009
#define INF 1000000007
#define imx 2147483647
#define LLINF 1000000000000000007
#define mp(x,y) make_pair(x,y)
#define wr cout<<"Continue Debugging!!!"<<endl;
#define ff first
#define ss second
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
#define ppb() pop_back()
#define tr(i, c) for(typeof((c).begin()) i = (c).begin(); i!=(c).end(); i++)
using namespace std;
typedef long long ll;
typedef pair<int,int>PII;
template<class T> bool umin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool umax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
int vis[12],flood=0;
void calc(int x){
	if(!x)
		vis[0]=1;
	while(x>=1){
		if(!vis[x%10])
			flood++;
		vis[x%10]++;	
		x/=10;
	}
}
int main(){
	freopen("love.in", "r", stdin);
	freopen("love.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		ll x;flood=0;
		fill(vis,vis+10,0);
		scanf("%lld",&x);
		if(!x){
			printf("Case #%d: INSOMNIA\n",i);
			continue;
		}
		for(ll j=x;j<LLINF;j+=x){
			calc(j);
			if(flood==10){
				printf("Case #%d: %lld\n",i,j);
				break;
			}
		}
	}
	return 0;
}
	

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
int main(){
	freopen("IloveYou.in", "r", stdin);
	freopen("IloveYou.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		ll n,k,s,h=1;
		scanf("%lld%lld%lld",&n,&k,&s);
		printf("Case #%d: ",i);
		for(int i=1;i<s;i++)
			printf("%d ",i);
		for(int i=1;i<=k;i++)
			h*=n;	
		printf("%lld\n",h);	
	}
	return 0;
}


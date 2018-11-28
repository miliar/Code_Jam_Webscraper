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
int arr[MAXN];
int t,n,k;
ll h[11],g[11];
ll tap(ll x){
	for(int i=2;i<=sqrt(x);i++)
		if(x%i==0)
			return i;
	return -1;		
}
void fun(int x){
	if(x>n){
		for(int i=2;i<=10;i++)
			h[i]=1;	
		for(int i=2;i<=n;i++)
			for(int j=2;j<=10;j++)
				h[j]=h[j]*j+arr[i];
		for(int i=2;i<=10;i++){
			int fup=tap(h[i]);
			if(fup==-1)
				return;g[i]=fup;
		}
		for(int i=1;i<=n;i++)
			printf("%d",arr[i]);	
		for(int i=2;i<=10;i++)
			printf(" %d",g[i]);
		printf("\n");k--;	
		if(!k)
			exit(0);
		return;
	}
	for(int i=0;i<2;i++){
		if(x==n and !i)
			continue;
		arr[x]=i;
		fun(x+1);
	}
}
int main(){
	//~ freopen("JavaIsTooSimple.in", "r", stdin);
	freopen("JavaIsTooSimple.out", "w", stdout);
	scanf("%d%d%d",&t,&n,&k);
	arr[1]=1;printf("Case #1:\n");fun(2);
	return 0;
}


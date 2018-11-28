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
int arr[11],pr[11],love[MAXN],done,a,vis[11];
int ok(int x){
	for(int i=2;i<x;i++)
		if(love[pr[i]]!=pr[i-1] and love[pr[i]]!=pr[i+1])
			return 0;	
	if(love[pr[1]]!=pr[2] and love[pr[1]]!=pr[x])
		return 0;	
	if(love[pr[x]]!=pr[x-1] and love[pr[x]]!=pr[1])
		return 0;		
	return 1;	
}
void len(int p,int x){
	if(done)
		return;
	if(p>x){
		//	for(int i=1;i<=x;i++)
		//		cout<<pr[i]<<" ";
		//	cout<<endl;	
		if(ok(x)){
			done=1;
		}
		return;		
	}
	for(int i=1;i<=a;i++){
		if(vis[i])
			continue;
		vis[i]=1;	
		pr[p]=i;len(p+1,x);
		vis[i]=0;
	}
}
int main(){
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		memset(love,0,sizeof(love));
		int g;
		scanf("%d",&a);
		for(int i=1;i<=a;i++)
			scanf("%d",&g),love[i]=g;
		pr[1]=4,pr[2]=3,pr[3]=2;
		int mx=1;	done=0;
		for(int i=a;i>1;i--){
			len(1,i);
			if(done){
				umax(mx,i);
				break;
			}
		}
		printf("Case #%d: %d\n",test,mx);	
	}
	return 0;
}



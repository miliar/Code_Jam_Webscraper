#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cin.tie(0);
using namespace std;
#define pb push_back
#define pob pop_back
#define pf push_front
#define pof pop_front
#define mp make_pair
#define all(a) a.begin(),a.end()
#define bitcnt(x) __builtin_popcountll(x)
#define MOD 1000000000
#define MAXN 500005
typedef unsigned long long int uint64;
typedef long long int int64;

int a[1011];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,m,i;
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>m;
		for(i=1;i<=m;i++)
		cin>>a[i];
		int maxi=0,ans1=0,ans2=0;
		for(i=2;i<=m;i++){
			maxi=max(maxi,a[i-1]-a[i]);
			ans1+=max(0,a[i-1]-a[i]);
		}
		for(i=1;i<m;i++){
			ans2+=min(a[i],maxi);
		}
		printf("%d %d\n",ans1,ans2);
		
	}
	fclose(stdout);
}

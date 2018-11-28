// adijimmy
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int mod = 1e9+7;
#define MAX 1005
int X,R,C;
ll power(ll a,ll b){
 ll res = 1;
 while(b){
	if(b&1) res = (res*a)%mod;
	a = (a*a)%mod;
	b >>= 1;
 }
 return res;
}
int arr[1005];
int main(){
	int t,n,m;
	freopen("bhubhu.in","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++){
	  int res1 = 0, res2 = 0;
	  printf("Case #%d: ",cas);
     scanf("%d",&n);
     for(int i=0;i<n;i++) scanf("%d",&arr[i]);
	  for(int i=1;i<n;i++){
		if(arr[i]<=arr[i-1]) res1 += arr[i-1]-arr[i];
	  }
	  int maxi = 0;
	  for(int i=1;i<n;i++){
		if(arr[i]<=arr[i-1]) maxi = max(maxi,arr[i-1]-arr[i]);
	  }
	  for(int i=0;i<n-1;i++){
		 if(arr[i]>=maxi) res2 += maxi;
		 else res2 += arr[i];
	  }
	  cout << res1 << " " << res2 << endl;
	}
	return 0;
}


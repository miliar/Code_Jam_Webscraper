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

int main(){
	int t,r,c,w;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int cas=1;cas<=t;cas++){
		printf("Case #%d: ",cas);
		cin>>r>>c>>w;
		int val=c/w;
		int ans=(r-1)*val+val+w-1;
		if(c%w)
		ans++;		
		cout<<ans<<endl;
	}
	fclose(stdout);
	return 0;
}

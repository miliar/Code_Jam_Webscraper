#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define inf 0x7fffffff
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define pr pair<int,int>
#define mp(a,b) make_pair(a,b)
#define pb push_back
#define fr first
#define sc second
#define mset(arr,val) memset(arr,val,sizeof(arr));

const int MAX = 1000005;
const int MOD = 1e9+7;

ll getMaxDigNum(ll val){
	int cnt = 0;
	std::vector< bool > pre(11,false);
	ll i;
	for(i = 1;i<=100 && cnt<10;i++){
		ll n = val*i;
		while(n){
			if(!pre[n%10]){
				cnt++;
				pre[n%10]= true;
			}
			n/=10;
		}
		if(cnt == 10) break;
	}
	return i*val;
}

int main(){
	// freopen("","r",stdin);
	// freopen("output.txt","w",stdout);
	int t;
	SCD(t);
	for(int i =1;i<=t;i++){
		ll n;
		SCLLD(n);
		if(n!=0)
			printf("Case #%d: %lld\n",i,getMaxDigNum(n));
		else{
			printf("Case #%d: INSOMNIA\n",i);
		}
	}
}
#include<bits/stdc++.h>

using namespace std;

#define ll unsigned long long

ll bm(ll k, ll c){
	ll res = 1;
	while(c){
		res*=k;
		c--;
	}
	return res;
}

int main(){
	freopen("inp.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	ll k,c,s;
	scanf("%d",&t);
	int tc = 0;
	while(t--){
		scanf("%llu %llu %llu",&k ,&c ,&s);
		ll pat = bm(k,c-1);
		//cout<<pat<<endl;
		printf("Case #%d: 1",++tc);
		for(ll i = 1; i < k; i++){
			printf(" %llu",i*pat + 1LL);
		} 
		puts("");
	}
}

#include <bits/stdc++.h>



using namespace std;



#define fr(i,a,b) for(int i=a;i<b;++i)
typedef pair<int,int> pii;
typedef long long ll;
#define F first
#define S second
#define mp make_pair




int n,t;
ll p,q,r,s;
ll qt[1000100];
ll ac[1000100];
ll tot;

ll get(int a, int b){
	if(a > b) return 0;
	ll ret = ac[b];
	if(a) ret -= ac[a-1];
	return ret;
}

ll scot(int a, int b){
	if(a > b) return tot;
	return max(max(get(0,a-1),get(b+1,n-1)),get(a,b));
}


int main(){
	scanf("%d",&t);
	fr(cas,1,t+1){
		tot = 0LL;
		printf("Case #%d: ",cas);
		scanf("%d %lld %lld %lld %lld",&n,&p,&q,&r,&s);
		fr(i,0,n){
			qt[i] = (i*p + q)%r + s;
			ac[i] = qt[i];
			if(i) ac[i] += ac[i-1];
			tot += qt[i];
//			printf("%lld ",qt[i]);
		}
//		puts("");
		int p2 = 0;
		ll ans = 0LL;
//		printf("%lld\n",tot);
		fr(p1,0,n){
			while(p2 < n && scot(p1,p2) <= scot(p1,p2-1)){ 
//				printf("%d %d %lld %lld\n",p1,p2,get(p1,p2),tot);
				p2++;
			}
			ll ot = scot(p1,p2-1);
//			printf("%d %d %lld %.10lf\n",p1,p2,tot,(tot-ot)/double(tot));
			ans = max(ans, tot-ot);
		}
		printf("%.10lf\n",ans/double(tot));
	}
	return 0;
}





































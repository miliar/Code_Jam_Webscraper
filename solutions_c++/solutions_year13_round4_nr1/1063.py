#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;


int mod = 1000002013;

int main(){
	int T;
	scanf("%d", &T);
	for(int TT = 1; TT <=T; TT++){
		int n, m;
		scanf("%d%d", &n, &m);
		int oo[110]={0};
		int ee[110]={0};
		int t[110]={0};
		long long expcost = 0;
		for(int i=0;i<m;i++){
			int o,e,p;
			scanf("%d%d%d", &o, &e, &p);
			if(o != e){
				int x=e-o;
				expcost += ((n+n-x+1)*x/2)*p;
			}
			oo[o]+=p;
			ee[e]+=p;
		}
		
		long long realcost = 0;
		for(int i=1;i<=n;i++){
			if(oo[i]){//ÓÐÈË½ø
				int x = min(oo[i], ee[i]);
				oo[i] -= x;
				ee[i] -= x;
			}
			for(int j=n; j>=2 && ee[i];j--){
				if(t[j] > 0){
					int x = min(t[j], ee[i]);
					t[j] -= x;
					ee[i] -=x;
				}
			}
			for(int j=2; j<n ;j++){
				t[j] = t[j+1];
				realcost += t[j]*j;
			}
			t[n] = oo[i];
			realcost += oo[i]*n;
			realcost %= mod;
		}

		printf("Case #%d: %d\n", TT, ((expcost-realcost)%mod+mod) % mod);
	}
}
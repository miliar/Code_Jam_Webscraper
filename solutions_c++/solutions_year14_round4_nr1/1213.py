#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int s[20000], u[20000];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        
		int n, m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++){
			scanf("%d",&s[i]);
			u[i]=0;
		}
		sort(s,s+n);
		int ans;
		for(ans=0;;ans++){
			int cap = m, k = 2;
			for(int i=n-1;i>=0;i--){
				if(k==0) break;
				if(u[i]==1) continue;
				if(cap >= s[i]){
					k--;
					u[i] = 1;
					cap -= s[i];
				}
			}
			if(cap == m) break;
		}
		
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}


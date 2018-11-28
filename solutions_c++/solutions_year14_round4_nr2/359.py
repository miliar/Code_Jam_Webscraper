#include<bits/stdc++.h>
#include<ext/rope>
#define f first
#define s second
using namespace std;
using namespace __gnu_cxx;
typedef pair<int,int>par;
rope<int> rp;
int main(){
	int T,t=0;
	scanf("%d",&T);
	while(T--){t++;
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			int k;
			scanf("%d",&k);
			rp.push_back(k);
			}
		int ans=0;
		for(int i=0;i<n;i++){
			int mi=0x7fffffff,p=0;
			for(int j=0;j<n-i;j++){
				if(rp[j]<mi)mi=rp[j],p=j;
				}
			ans+=min(p,n-i-p-1);
			rp.erase(p,1);
			}
		printf("Case #%d: %d\n",t,ans);
		}
    return 0;
    }

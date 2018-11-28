#include <cstdio>
#include <algorithm>

using namespace std;

int s[11111];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,ti,n,x,i,begin,end,ans;
	scanf("%d",&t);
	for(ti=1;ti<=t;ti++){
		scanf("%d%d",&n,&x);
		for(i=0;i<n;i++){
			scanf("%d",&s[i]);
		}
		sort(s,s+n);
		ans=0;
		begin=0; end=n-1;
		while(begin<end){
			if(s[begin]+s[end]<=x){
				ans++; begin++; end--;
			}else{
				ans++; end--;
			}
		}
		if(begin==end){
			ans++;
		}
		printf("Case #%d: %d\n",ti,ans);
	}
}
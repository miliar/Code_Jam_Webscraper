#include <bits/stdc++.h>
using namespace std;



bool vis[11];

bool judge(){
	for(int i=0;i<10;i++){
		if(!vis[i])return 0;
	}
	return 1;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		cas++;
		memset(vis,0,sizeof(vis));
		
		int n;
		cin>>n;
		
		int ans = -1;
		for(int i=1;i<=1000;i++){
			int cur = n*i;
			while(cur){
				vis[cur%10] = 1;
				cur/=10;
			}
			if(judge()){
				ans=n*i;
				break;
			}
		}
		
		if(~ans){
			printf("Case #%d: %d\n",cas,ans);
		}else{
			printf("Case #%d: INSOMNIA\n",cas);
		}
	}
	
	return 0;
}

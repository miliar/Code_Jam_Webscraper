#include <bits/stdc++.h>
using namespace std;
bool vis[20];
bool check(){
	for(int i=0;i<10;i++)
		if(!vis[i])
			return 0;
	return 1;
}
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int tt,n,ans,cot=1;
	scanf("%d",&tt);
	while(tt--){
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",cot++);
		else{
			ans=0;
			memset(vis,0,sizeof(vis));
			while(!check()){
				ans+=n;
				int c=ans;
				while(c){
					vis[c%10]=1;
					c/=10;
				}
			}
			printf("Case #%d: %d\n",cot++,ans);
		}
	}
	//system("pause");
	return 0;
}
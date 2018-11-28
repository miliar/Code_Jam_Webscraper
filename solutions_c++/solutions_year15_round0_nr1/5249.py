#include<bits/stdc++.h>
using namespace std;
int main(){
	int t;
	scanf("%d",&t);
	int y=1;
	while(t--){
		char s[1005];
		int smax;
		scanf("%d",&smax);
		getchar();
		scanf("%s",&s);
		int tn=0,ans=0;
		for(int i=0;i<=smax;i++){
			if(s[i]>'0'){
				if(tn>=i){
					tn=tn+(s[i]-'0');
				}
				else{
					ans+=(i-tn);
					//printf("%d %d %d",i,(i-tn),tn);
					tn=tn+(s[i]-'0')+(i-tn);
				}
			}
		}
		printf("Case #%d: %d\n",y,ans);
		y++;
	}
}

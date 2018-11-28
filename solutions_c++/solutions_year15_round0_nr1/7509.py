#include<bits/stdc++.h>
using namespace std;
int main(){
	int t,n,count,i,ans,j;
	char s[1005];
	scanf("%d",&t);
		for(j=1;j<=t;j++){
		ans=0;
		count=0;
		scanf("%d %s",&n,s);
		if(s[0]-'0'==0){
			count++;
			ans++;
		}
		else{
			count+=s[0]-'0';
		}
		for(i=1;i<=n;i++){
			if(s[i]-'0'>0){
				if(count>=i)
					count+=s[i]-'0';
				else{
					ans+=i-count;
					count+=(i-count)+s[i]-'0';
				}
			}
		}
		printf("Case #%d: %d\n",j,ans);
		
	}
	return 0;
}

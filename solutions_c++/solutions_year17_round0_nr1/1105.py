#include <bits/stdc++.h>
using namespace std;
int cake[1010];
int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;t++){
		string s;
		int x;
		cin>>s>>x;
		for(int i=0;i<s.size();i++){
			if(s[i]=='+') cake[i]=1;
			else cake[i]=0;
		}
		int ans=0;
		for(int i=0;i+x-1<s.size();i++){
			if(!cake[i]){
				ans++;
				for(int j=i;j<i+x;j++){
					cake[j]^=1;
				}
			}
		}
		int valid=1;
		for(int i=0;i<s.size();i++){
			if(!cake[i]) valid=0; 
		}
		if(valid) printf("Case #%d: %d\n",t,ans);
		else printf("Case #%d: IMPOSSIBLE\n",t);

	}
}
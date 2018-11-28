#include <bits/stdc++.h>
using namespace std;


char str[111];


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		cas++;
		scanf("%s",str);
		int len = strlen(str);
		
		int ans = 0;
		
		int pos = 0;
		if(str[pos]=='-'){
			while(str[pos]=='-'){
				pos++;
			}
			ans++;
		}
		
		while(pos<len){
			if(str[pos]=='-'){
				while(str[pos]=='-'){
					pos++;
				}
				ans+=2;
			}
			pos++;
		}
		
		printf("Case #%d: %d\n",cas,ans);
		
	}
	
	return 0;
}

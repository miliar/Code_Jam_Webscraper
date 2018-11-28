#include <bits/stdc++.h>
using namespace std;


int main(){
	int t; scanf("%d",&t);
	for(int caso = 1; caso <= t; caso++){
		int n; scanf("%d",&n);
		string s; cin >> s;
		int acu = 0, ans = 0;
		for(int i = 0; i < s.length(); i++){
			if(s[i] == '0'){
				continue;
			}else{
				if(acu >= i){
					acu += s[i]-48;
				}else{
					ans += i-acu;
					acu += s[i]-48 +i-acu ;
				}				
			}
		}
		printf("Case #%d: %d\n",caso,ans);
	}
	return 0;
}
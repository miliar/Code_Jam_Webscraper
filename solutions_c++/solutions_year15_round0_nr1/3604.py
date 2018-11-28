#include<bits/stdc++.h>

using namespace std;

int main(){
	int T, n;
	string s;
	freopen("A2.in","r",stdin);
	freopen("A.out","w",stdout);
	
	cin >> T;
	
	for(int tc = 1; tc <= T; tc ++){
	
		cin >> n;
		
		cin >> s;
		
		int total = 0, ans = 0;
		
		for(int i = 0; i < s.size(); i ++){
		
			if(total >= i){
				total += s[i] - '0';
			}else{
				ans += i - total;
				total += i - total;
				total += s[i] - '0'; 
			}
		}
	
		printf("Case #%d: %d\n",tc, ans);
	}
	return 0;
}

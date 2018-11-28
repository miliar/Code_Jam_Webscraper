#include "bits/stdc++.h"
using namespace std;
int main(){
	int t; scanf("%d", &t);
	int i;
	for(i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		int n; cin>>n;
		string s;
		cin>>s;
		int j;
		int c = 0;
		int ans = 0;
		for(j = 0; j < n+1; j++){
			int num =  s[j]-'0';
			if(c < j && num != 0){
				ans += j-c;
				c = num + j;
			}
			else if(num != 0){
				c += num;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
